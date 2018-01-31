#JB Fasquel
import cv2
import numpy as np
import mido

############
# MIDI part
import mido,time
print(mido.get_output_names())
out_names=mido.get_output_names()
outport = mido.open_output(out_names[0])

############
# GUI part
capture = cv2.VideoCapture(0)
while(capture.isOpened()): #e.g. cam unplugged
    ret, image = capture.read()
    if ret:
        image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY).astype(np.uint8) #BGR because opencv images are BGR and not RGB
        val=np.mean(image_gray)
        print(val,np.max(image_gray),np.min(image_gray))
        val_note=int(np.round(val*127/255))
        outport.send(mido.Message('note_on', channel=0, note=val_note, velocity=100, time=0))
        #time.sleep(0.5)
        cv2.imshow("Video", image)
        key=cv2.waitKey(8)
        if key == 27: #27: Escape key
            break #On sort de la boucle de lecture/affichage
    else:break

#Release everything if job is finished
capture.release()
cv2.destroyAllWindows()