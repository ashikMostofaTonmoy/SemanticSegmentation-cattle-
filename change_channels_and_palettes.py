# %%
import os.path as osp
import mmcv
import numpy as np
import cv2
from PIL import Image 

# for file in mmcv.scandir(osp.join(data_root, ann_dir), suffix='.regions.txt'):
#   seg_map = np.loadtxt(osp.join(data_root, ann_dir, file)).astype(np.uint8)
#   seg_img = Image.fromarray(seg_map).convert('P')
#   seg_img.putpalette(np.array(palette, dtype=np.uint8))
#   seg_img.save(osp.join(data_root, ann_dir, file.replace('.regions.txt', 
#                                                          '.png')))
# %%
# for file in mmcv.scandir('annotations', suffix='.png'):
#     file_name =  file.split('.')[0] + '.png'
#     # print(f"{file_name}")
    
#     img = cv2.imread(osp.join('annotations', file) , cv2.IMREAD_UNCHANGED)
#     # print(img.shape)
#     # In case of grayScale images the len(img.shape) == 2
#     if len(img.shape) > 2 and img.shape[2] == 4:
#         #convert the image from RGBA2RGB
#         # img_bgr = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
#         # img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
#         img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
#         # print(img.shape)
#         cv2.imwrite(osp.join('changed_channel', file_name), img)
        
#         # changed_channel
#         im2 = cv2.imread(osp.join('changed_channel', file_name) , cv2.IMREAD_UNCHANGED)
#         # print(im2.shape)
#     # break
# %%
for file in mmcv.scandir('annotations', suffix='.png'):
    file_name =  file.split('.')[0] + '.png'

    img = cv2.imread(osp.join('annotations', file) , cv2.IMREAD_UNCHANGED)
    if len(img.shape) > 2 and img.shape[2] == 4:
        #convert the image from RGBA2RGB
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        cv2.imwrite(osp.join('changed_channel', file_name), img)
# %%
# print("done!")
# %%
palette = [[63, 100, 24], [133, 74, 39], [214 ,84, 211], [223 , 71, 154], 
           [120, 180, 248], [51, 95, 247] , [210, 69, 36]]
for file in mmcv.scandir('changed_channel', suffix='.png'):
#     file_name =  file.split('.')[0] + '.png'
    print(f"{file}")
    # seg_img = Image.open(osp.join('changed_channel',file ))
    # print(seg_img.mode)
    seg_img = Image.open(osp.join('changed_channel',file )).convert("P",dither= None, palette= 1 , colors= 7 )
    # print(type(seg_img))
    # seg_img.putpalette(palette)
    seg_img.save(osp.join('change2pallets', file))


    # break
# %%
print("done!")
# %%
# for file in mmcv.scandir('change2pallets', suffix='.png'):
# #     file_name =  file.split('.')[0] + '.png'
#     print(f"{file}")
#     # seg_img = Image.open(osp.join('changed_channel',file ))
#     # print(seg_img.mode)
#     seg_img = Image.open(osp.join('change2pallets',file )).convert("RGB",dither= None, palette= 1 , colors= 7 )
#     # print(type(seg_img))
#     # seg_img.putpalette(palette)
#     seg_img.save(osp.join('palette2rgb', file))


#     break
# %%
