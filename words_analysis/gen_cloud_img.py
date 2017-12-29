# -*- coding: UTF-8 -*-

from wordcloud import WordCloud
from wordcloud import ImageColorGenerator as gengerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


mlist = {}

with open('./android.txt', "r") as f:
    '''
    读取单词文本 将文本读取为字典格式
    {}
    '''
    for i in f.readlines():
        m = i.split(":")
        mlist[m[0]] = int(m[1].strip('\n'))


alice_coloring = np.array(Image.open('../image/python_img.jpg'))

wc1 = WordCloud(
    max_words=8000,
    mask=alice_coloring,
    background_color="black",
    scale=2)

image_colors = gengerator(alice_coloring)

wc2 = wc1.generate_from_frequencies(mlist)
wc2.to_file("../image/python_img_com_s2.png")

# plt.imshow(wc2.recolor(color_func=image_colors), interpolation="bilinear")
plt.imshow(wc2)
plt.axis("off")
plt.show()



