import numpy as np
from PIL import Image

radar = np.load('./origin_data/radars_2020-11-01_2022-12-31.npy')
color_image = Image.open('./cool_data/mask.png')

mask = np.array(color_image.convert('L'))
for i in range(825):
    for j in range(200):
        if mask[i, j] > 200:
            mask[i, j] = 0
        else:
            mask[i, j] = 1

index = 0
ice = np.array(radar)
for index in range(radar.shape[0]):
    for i in range(825):
        for j in range(200):
            if radar[index, i, j] > 0.53:
                ice[index, i, j] = 1
            else:
                ice[index, i, j] = 0
    ice[index] = ice[index]*mask
    print(index)

np.save('./cool_data/ice_mask.npy',ice)

