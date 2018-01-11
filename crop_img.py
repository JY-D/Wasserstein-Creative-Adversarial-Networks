import glob
import numpy as np
import cv2
import pdb

for CAN_sample in glob.glob('./logs/dataset=wikiart,isCan=True,lr=0.0001,imsize=128,batch_size=35/003/samples/train_03*'):
    print ('now cropping ', CAN_sample)
    img = cv2.imread(CAN_sample)
    #print(np.shape(img))
    for i in range (8):
        i = i * 128
        #pdb.set_trace()
        #print (i)
        for j in range (9):
            j = j * 128
            #print(j)
            #print (np.shape(img[i:i+128, j: j+128,:]))
            filename = './logs/dataset=wikiart,isCan=True,lr=0.0001,imsize=128,batch_size=35/003/samples/crop/{0}_{1}_{2}.png'.format(CAN_sample[-13:-4] ,i, j)
            print (filename)
            cv2.imwrite(filename ,img[i:i+128, j: j+128,:])    

for WCAN_sample in glob.glob('./logs/dataset=wikiart,isCan=True,lr=0.0001,imsize=128,batch_size=35/004/samples/train_05*'):
    print ('now cropping', WCAN_sample)
    img = cv2.imread(WCAN_sample)
    #print(np.shape(img))
    for i in range (8):
        i = i * 128
        #pdb.set_trace()
        #print (i)
        for j in range (9):
            j = j * 128
            #print(j)
            #print (np.shape(img[i:i+128, j: j+128,:]))
            filename = './logs/dataset=wikiart,isCan=True,lr=0.0001,imsize=128,batch_size=35/004/samples/crop/{0}_{1}_{2}.png'.format(WCAN_sample[-13:-4] ,i, j)
            print (filename)
            cv2.imwrite(filename ,img[i:i+128, j: j+128,:])

