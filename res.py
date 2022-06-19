import os
import cv2
import numpy as np

in_file = "db1039.jpg"
opn = os.listdir('./open/')

data = os.listdir('./res/')
for openf in opn:
    for files in data:
        img_rgb = cv2.imread("./open/"+openf) #Где ищем
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread("./res/" + files, 0) #Что ищем
        w, h = template.shape[::-1]
        
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)
        print(len(loc))
        s = 0
        if  len(loc) > 0:
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
                #print('rectangle')
                print(pt)
                s+=1            
            print(s/54)
            cv2.imwrite(r'./fin/'+openf +"_"+"_"+ files, img_rgb) # Запись результатов
#cv2.imshow('result', img_rgb)
#cv2.waitKey(0)
