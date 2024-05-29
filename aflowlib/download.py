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

    link_size = len(link_list)
    # save link_list
    csv_file = f"{local_file.split('.')[0]}-{str(link_size)}.csv"
    with open(csv_file, 'w') as link_file:
        write_content = '\n'.join(link_list)
        link_file.write(write_content)
    return csv_file


# get line with 'aflowlib_entries' and save to AgAl.html
# 其中第一个href是不要的，手动删除
def subtrat_href(download_file='2-AgAl.html', local_file=None):
    with open(download_file, 'r') as html_file:
        for line in html_file.readlines():
            if line.__contains__('>aflowlib_entries<'):
                with open(local_file, 'w') as AgAl_file:
                    AgAl_file.write(line)
                break
    return local_file


import os

if __name__ == '__main__':
    if os.path.exists('dataset') is False:
        os.mkdir('dataset')
    # download html file from csv file link, 命名为2-AgAl.html为例
    except_files = []
    with open('aflowlib-lib2-1706.csv', 'r') as urls_file:
        for material_link in urls_file.readlines()[85:]:            # 因为AgO中断了，所以手动从这里继续下载
            # https://aflowlib.duke.edu/AFLOWDATA/LIB2_WEB/./AgAl/
            download_file = f"dataset/2-{material_link.split('/')[-2]}.html"        # 2-AgAl.html
         
            # wait for download
            subprocess.call(f"curl -o {download_file} {material_link}", shell=True)

            # ToDo use shell command substrat a line containing 'aflowlib_entries' and '<br>' to a new file, e.g. AgAl.html
            # 这一步网页可能不符合预期，local_file is None
            local_file = f"dataset/3-{material_link.split('/')[-2]}.html"
            subtrat_href(download_file, local_file)
            try:
                # now we can get_link from 3-AgAl.html and save to 3-AgAl-xxx.csv
                csv_file = get_link(material_link, local_file)
                with open(csv_file, 'r') as subset_urls:
                    # https://aflowlib.duke.edu/AFLOWDATA/LIB2_WEB/AgAl/./1/
                    for item in subset_urls:
                        save_item = f"dataset/{item.split('/')[-4]}-{item.split('/')[-2]}.html"
                        # skip if file already exists
                        if os.path.exists(save_item):
                            continue
                        subprocess.call(f"curl -o {save_item} {item}", shell=True)
            except FileNotFoundError:
                print(f"{local_file} not found.")
                except_files.append(local_file)
    if len(except_files) > 0:
        print(f"获取材料页面脚本出错，出错数目：{len(except_files)}")
        print(f"出错文件为：")
        print('\n'.join(except_files))
        print(f"请根据README.md手动修改或增加代码修复。")

