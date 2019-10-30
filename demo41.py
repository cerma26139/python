#kakaku
#ctrl+alt+m  變成函數
from urllib import request
from PIL import Image
url1 = 'https://img3.momoshop.com.tw/goodsimg/0005/568/345/5568345_L.jpg?t=1535419805'


def saveImage(url,path):
    file1 = request.urlopen(url)
    image1 = Image.open(file1)
    image1.save(path)


saveImage(url1,'images\\sample3.jpg')