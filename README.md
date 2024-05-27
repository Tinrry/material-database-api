## information
1. OQMD--OK, download by yang, need mysql service .
2. NOMAD
   [学习链接](https://www.nomad-coe.eu/events2/course-on-big-data-and-artificial-intelligence/exercise-1)

   是AFLOW的子集
   
   使用方法见nomad.ipynb
   ```
   ```
   里面有大量的workflow配置文件，不干净。

查看一下paper rank上面关于上面数据库的研究进展

## AFLOW
DISCLAIMER
The data included within the aflow.org repository is free for scientific, academic and non-commercial purposes. Any other use is prohibited.
AFLOW and AFLOWLIB.ORG come with ABSOLUTELY NO WARRANTY, to the extent permitted by applicable law.

整体的数据集
https://aflowlib.duke.edu/AFLOWDATA/LIB2_WEB/

获取该网站数据集的方法：
1. 从一级目录  https://aflowlib.duke.edu/AFLOWDATA/LIB2_WEB/  获取所有材料的元素，保存在aflowlib-lib2-1706.csv.
2. 从第一步获取1706个二级目录的链接,记录每个元素的所有具体材料网页的链接，比如AgAl-1057.csv, 表示元素比如AgAl有1057个材料页面。
3. 下载材料页面，比如AgAl-1057.csv，有1057个html网页。其中一个页面示例为：aflowlib-AgAl-1
从这里我们可以算出，一个页面26k * 1000000 = 26G 文件大小

相关文件在文件夹aflowlib中，完整数据集在dataset中（local）