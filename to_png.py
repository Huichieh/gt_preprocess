import os
import numpy as np
# import SimpleITK as sitk
from torchvision import transforms
toPIL = transforms.ToPILImage()

path = "E:/gt_new/"
new_path = "E:/gt_png/"
if not os.path.isdir(new_path):
    os.mkdir(new_path)

def normalize(image):
    return (image-image.min())/(image.max()-image.min())

filename_list = os.listdir(path)

for file in filename_list:
    rawImg = np.fromfile(os.path.join(path, file), dtype=np.float32)
    pic_gray = rawImg.reshape([512,512])
    pic_gray = normalize(pic_gray) * 255
    pic_gray = pic_gray.astype(np.uint8)
    im = toPIL(pic_gray)
    im.save('{}/{}.png'.format(new_path, file.split('.')[0]))
    print('{}.png saved!'.format(file.split('.')[0]))
