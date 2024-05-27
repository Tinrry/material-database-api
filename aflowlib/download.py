# 以https://aflowlib.duke.edu/AFLOWDATA/LIB2_WEB/AgAl/目录为例，自动下载下面的1057个链接。
from bs4 import BeautifulSoup
import subprocess


def get_link(base_url, local_file):
    # base_url = 'https://aflowlib.duke.edu/AFLOWDATA/LIB2_WEB/AgAl/'
    # 手动下载base_url, 将'aflowlib_entries'和'<br>'之间的内容保存到AgAl.html
    with open(local_file, 'r') as html_file:
        content = html_file.read()
    soup = BeautifulSoup(content, 'html.parser')
    
    # 末尾加/
    # 去掉第一个href
    link_list = []
    for link in soup.find_all('a')[1:]:
        link_list.append(''.join([base_url.strip(), link.get('href').strip(), '/']))
        # debug
        if len(link_list) == 5:
            break

    link_size = len(link_list)
    # save link_list
    csv_file = f"{local_file.split('.')[0]}-{str(link_size)}.csv"
    with open(csv_file, 'w') as link_file:
        write_content = '\n'.join(link_list)
        link_file.write(write_content)
    return csv_file


# get line with 'aflowlib_entries' and save to AgAl.html
# 其中第一个href是不要的，手动删除
def subtrat_href(download_file='2-AgAl.html', save_file='3-AgAl.html'):
    with open(download_file, 'r') as html_file:
        for line in html_file.readlines():
            if line.__contains__('>aflowlib_entries<'):
                with open(save_file, 'w') as AgAl_file:
                    AgAl_file.write(line)
                break
    return save_file



if __name__ == '__main__':
    # download html file from csv file link, 命名为2-AgAl.html为例
    with open('aflowlib-lib2-1706.csv', 'r') as urls_file:
        for material_link in urls_file:
            # https://aflowlib.duke.edu/AFLOWDATA/LIB2_WEB/./AgAl/
            save_name = f"2-{material_link.split('/')[-2]}.html"        # 2-AgAl.html
            # wait for download
            subprocess.call(f"curl -o {save_name} {material_link}", shell=True)
            # ToDo use shell command substrat a line containing 'aflowlib_entries' and '<br>' to a new file, e.g. AgAl.html
            download_file = save_name
            save_file = f"3-{material_link.split('/')[-2]}.html"
            subtrat_href(download_file, save_file)
            # now we can get_link from 3-AgAl.html and save to 3-AgAl-xxx.csv
            base_url = material_link
            local_file = save_file
            csv_file = get_link(base_url, local_file)
            with open(csv_file, 'r') as subset_urls:
                # https://aflowlib.duke.edu/AFLOWDATA/LIB2_WEB/AgAl/./1/
                for item in subset_urls:
                    save_item = f"{item.split('/')[-4]}-{item.split('/')[-2]}.html"
                    subprocess.call(f"curl -o {save_item} {item}", shell=True)
                    # for debug
                    break
            break

