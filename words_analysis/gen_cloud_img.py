# -*- coding: UTF-8 -*-

from wordcloud import WordCloud
from wordcloud import ImageColorGenerator as gengerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from scipy.misc import imread


mlist = {}
# with open('./cont.txt', "r") as f:
#     for i in f.readlines():
#         n = i.replace(":", ",")
#         with open('./new.txt',"a") as f1:
#             f1.write(n)
#
# with open('./new.txt', 'r') as f:
#     for i in f.readlines():
#         mlist.append(tuple(i))

with open('./cont.txt', "r") as f:
    for i in f.readlines():
        m = i.split(":")
        # a = (m[0], m[1].strip('\n'))
        mlist[m[0]] = int(m[1].strip('\n'))

print mlist
print type(mlist)


alice_coloring = np.array(Image.open('test.jpg'))

wc1 = WordCloud(
    max_words=8000,
    mask=alice_coloring,
    background_color="white",
    scale=10)

image_colors = gengerator(alice_coloring)

wc2 = wc1.generate_from_frequencies(mlist)
wc2.to_file("alice.png")

# plt.imshow(wc2.recolor(color_func=image_colors), interpolation="bilinear")
plt.imshow(wc2)
plt.axis("off")
plt.show()



