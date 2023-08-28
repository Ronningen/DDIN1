import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import Button
import datetime

#Полученние данных
zero_day = datetime.date(2020, 11, 1)
radar = np.load('./origin_data/radars_2020-11-01_2022-12-31.npy')
ocean = np.load('./cool_data/good_ocean.npy')
cool_data = np.load('./cool_data/good_data.npy')
ice = np.load('./cool_data/ice_mask.npy')
meta = np.load('./cool_data/meta_data.npy')

#Задание констант
index = 0
X = np.linspace(0, 199, 200)
Y = np.linspace(0, 824, 825)

def onclick(index):
    plt.clf()
    plt.imshow(radar[index]+ice[index], cmap='terrain', vmin=0.3, vmax=1.0)
    plt.streamplot(X, Y, ocean[index, 0], ocean[index, 1],
                   density=1.5, linewidth=0.7, color='Red')
    plt.text(300, 725, 'Day\'s passed: ' + str(meta[1, index]), va='center')
    plt.text(300, 675, 'Day: ' + str(meta[0, index]), va='center')
    plt.text(300, 625, 'Date: ' + str(zero_day +
             datetime.timedelta(days=index)), va='center')
    plt.draw()

def next_image(event):
    global index
    index = index+1
    while meta[2, index] == 0:
        index = index+1
    onclick(index)

def prev_image(event):
    global index
    index = index-1
    while meta[2, index] == 0:
        index = index-1
    onclick(index)

#Отрисовка
plt.imshow(radar[index]+ice[index], cmap='terrain', vmin=0.3, vmax=1.0)
plt.streamplot(X, Y, ocean[index, 0], ocean[index, 1],
               density=1.0, linewidth=1.0, color='Red')
plt.text(300, 725, 'Day\'s passed: ' + str(meta[1, index]), va='center')
plt.text(300, 675, 'Day: ' + str(meta[0, index]), va='center')
plt.text(300, 625, 'Date: ' + str(zero_day +
         datetime.timedelta(days=index)), va='center')


plt.connect('button_press_event', next_image)
plt.connect('key_press_event', prev_image)

plt.show()
