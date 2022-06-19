import numpy as np
import os 
import cv2


xz=0				   #Переменная нужна для создания уникальных файлов. 
def sim_xyz(c,x, img):
#Аргумент с-определение угла по ХZ в системе координат XYZ.
# Аргумент х- определение угла по YZ в системе координат XYZ.
    global xz
    hieght,width = img.shape[:2]			      #Высота и ширина изображения.
    for i in range(100):					   #Цикл для прогона скрипта.
        xz+=1      
# Отражение по оси XYZ.
        M = np.float32([[1,c,0],[x,1,0],[0,0,1]])		          #Преобразование углов. 
        res = cv2.warpPerspective(img, M,(int(hieght*2.3), int(width*2)))            #Объект подставляем в преобразованные углы.
        cv2.imwrite(r'./res/'+str(xz)+'_sim.png', res)   #Сохраняем измененное изображение. 
        xz+=1
# Зеркальное отражение. 
        flip_img = cv2.flip(res,1)				        #Отображаем зеркально. 
        cv2.imwrite(r'./res/'+str(xz)+'_sim.png', flip_img)  #Сохраняем объект. 
        xz+=1  
# Отображение по углам от -180 до 180 оси XY.         
        center = (width/2, hieght/2) 					#Высчитываем центр. 
        for i in range(0, 45, 10):    #Для каждго объекта будет применен угол от 0 до 45 по оси XY.       
            xz+=1
            m = cv2.getRotationMatrix2D(center, i, 1.0)#Вращение относительно центра на заданный угол. 
            rotated = cv2.warpAffine(res, m, (int(width*2.3),int(hieght*2)))      #Подставляем объект в заданные параметры. 
            flip_img_rot = cv2.flip(rotated,1)	      #Зеркальное отображение для каждого шага.
            cv2.imwrite(r'./res/'+str(xz)+'_sim.png', rotated) #Сохраняем. 
            xz+=1
            cv2.imwrite(r'./res/'+str(xz)+'_sim.png', flip_img_rot)						        #Сохраняем зеркальное отображение.  
        if c != 0:#Условие для изменения углов В оси  XYZ.
            c+=0.06
        if x != 0:
            x+=0.06
        if c >0.5 or x>0.5: # Если угол больше 0.5 выполнение цикла останавливается.
            break 
directory = os.listdir(r'./data')#Находим список необходимых файлов для поиска.
for file in directory: 			#Берем каждый файл из списка по отдельности.
    image = cv2.imread(r'./data/'+file)
    sim_xyz(c=0.02, x=0,img=image)
    sim_xyz(c=0, x=0.02,img=image)
    sim_xyz(c=0.02, x=0.02,img=image)
