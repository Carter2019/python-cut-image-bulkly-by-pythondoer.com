import os
from PIL import Image
path="D:\\图书馆\\Python脚本\\新建文件夹\\"
file_list=os.listdir(path)
print(file_list)
for file in file_list:
    
    img=Image.open(path+file)
    print(img.size)
    ratio=img.width/img.height
    img_resize=img.resize((500,500),Image.NEAREST)
    img_resize.save(path+"1"+file)
    
