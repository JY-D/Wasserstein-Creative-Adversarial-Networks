import glob
import numpy as np
import cv2
import pdb

canvas = np.zeros((384, 384, 3))

img = np.zeros((9, 128, 128, 3))

idx = 0
for sample in glob.glob('./*.png'):
    img[idx, :, :, :] = cv2.imread(sample)
    idx += 1

#pdb.set_trace()

idx = 0
for i in range (3):
    i = i * 128
    for j in range (3):
        j = j * 128
        #filename = './logs/dataset=wikiart,isCan=True,lr=0.0001,imsize=128,batch_size=35/003/samples/crop/{0}_{1}_{2}.png'.format(CAN_sample[-13:-4] ,i, j)
        #print (filename)
        #img = cv2.imread(sample)
        canvas[i:i+128, j: j+128,:] = img[idx, :, :, :]
        #cv2.imwrite(filename ,img[i:i+128, j: j+128,:])    
        idx += 1
#print (np.shape(canvas))
#pdb.set_trace()
cv2.imwrite('collect.png' , canvas)
