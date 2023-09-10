import streamlit as st
import cv2
import numpy as np
import cvzone
from cvzone.PoseModule import PoseDetector
from playsound import playsound
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sender_email = "haiseo352001@gmail.com"
sender_password = "oygznqlayprkfhsg"
receiver_email = "truonghai352001@gmail.com"
subject = "Hệ Thống Thị Giác Máy Tính Giám Sát Người Tập Thể Hình"

car = 0
car1 = 1
dir = 0
dir1 = 1
count = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
def write_data(file, data):
    f = open(file, "w")
    f.write(str(data))

def read_data(file):
    f = open(file, "r")
    result = f.read() 
    return result
detector = PoseDetector(detectionCon=0.69)
color = (0,0,255)
st.title("Hệ Thống Giám Sát Tập Thể Hình")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
cap = cv2.VideoCapture(0)

option = st.selectbox('Exercise',('Dumbbell Becips Curls','Squat'))
st.write('You selected:', option)

while run:   
        ret, frame  = cap.read()
        frame = detector.findPose(frame, draw=False)
        lmlist, bbox = detector.findPosition(frame, draw=False)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        write_data("checkrun.txt","run") 

        if lmlist:
                angle = detector.findAngle(frame, 11, 13, 15)
                bar_val = np.interp(angle,(10,170),(70,300+60))
                per_val = np.interp(angle,(10,170),(100,0))

                angle1 = detector.findAngle(frame, 16, 14, 12)
                bar_val1 = np.interp(angle1,(10,170),(70,300+60))
                per_val1 = np.interp(angle1,(10,170),(100,0))

                angle2 = detector.findAngle(frame, 28, 26, 24)
                bar_val2 = np.interp(angle2,(70,180),(100,300+60))
                per_val2 = np.interp(angle2,(70,180),(100,0))  
            
                if option =='Dumbbell Becips Curls':
            # tay trai
                        if 20 <= per_val <= 84 and car == 0:
                                count += 0.5
                                car = 1
                                color = (0, 255, 0)
                        elif 0<= per_val <= 10 and car == 1:
                                count += 0.5
                                car = 0
                                color = (0, 255, 0)
                                if car1 == 1:
                                        playsound('taytrais.mp3')
                        else:
                                color = (0,0,255)

                        if 85 <= per_val <= 100 and car1 == 1:
                                count1 += 0.5
                                car1 = 0
                                color = (255, 0, 0)
                        elif 0<= per_val <= 10 and car1 == 0:
                                count1 += 0.5
                                car1 = 1
                                color = (255, 0, 0)
                        else:
                                color=(0,0,255)
                        # tay phai 
                        
                        if 20 <= per_val1 <= 84 and dir == 0:
                                count2+=0.5
                                dir = 1
                                color = (0, 255, 0)
                        elif 0 <= per_val1 <= 10 and dir == 1:
                                count2+=0.5
                                dir = 0
                                color = (0, 255, 0)
                                if dir1 == 1:
                                        playsound('tayphai.mp3')
                        else:
                                color = (0,0,255)
                        
                        if 85 <= per_val1 <= 100 and dir1 == 1:
                                count3+=0.5
                                dir1 = 0
                                color = (255, 0, 0)
                        elif 0 <= per_val1  <= 10 and dir1 == 0:
                                count3+=0.5
                                dir1 = 1
                                color = (255, 0, 0)
                        else:
                                color=(0,0,255)
                        
                        print(int(count))
                        print(int(count1))
                        print(int(count2))
                        print(int(count3))

                        write_data("count.txt", count)
                        write_data("count1.txt", count1)
                        write_data("count2.txt", count2)
                        write_data("count3.txt", count3)
                                                                                                                                                                                                                                
                        cv2.rectangle(frame,(580,int(bar_val)),(0+620,300+60),color,cv2.FILLED)
                        cv2.rectangle(frame,(580,60),(0+620,300+60),(255,255,255),1)
                        cvzone.putTextRect(frame,f"{int(per_val)} %",(540,40),1.2,1,(255,255,255),color,border=1,colorB=())  
                        cvzone.putTextRect(frame,'Bicep Curl Exercise',(40,40),1.5,2,(255,255,255),(255,0,0),border=2,colorB=())
                        cvzone.putTextRect(frame,f'count : {int(count)}',(40,80),1.5,2,(0,0,0),(0,255,255),border=2,colorB=())
                        cvzone.putTextRect(frame,f'count1 : {int(count1)}',(40,120),1.5,2,(0,0,0),(0,255,255),border=2,colorB=())
                        cvzone.putTextRect(frame,f'count2 : {int(count2)}',(40,160),1.5,2,(0,0,0),(0,255,255),border=2,colorB=())
                        cvzone.putTextRect(frame,f'count3 : {int(count3)}',(40,200),1.5,2,(0,0,0),(0,255,255),border=2,colorB=())
                        cv2.rectangle(frame,(480,int(bar_val1)),(0+520,300+60),color,cv2.FILLED)
                        cv2.rectangle(frame,(480,60),(0+520,300+60),(255,255,255),1)
                        cvzone.putTextRect(frame,f"{int(per_val1)} %",(440,40),1.2,1,(255,255,255),color,border=1,colorB=())
                if option =='Squat': 
                        if 20<=per_val2 <=80 and dir==0:
                                count4 +=0.5
                                dir =1
                                color = (0,0,255)
                        elif 0<= per_val2 <=10 and dir == 1:
                                count4+=0.5
                                dir = 0
                                color = (0,0,255)
                                if dir1==1:
                                        playsound('dongtacsai.mp3')
                        else:
                                color =(0,0,225)
                        
                        if 81<=per_val2 <=100 and dir1==1:
                                count5 +=0.5
                                dir1 =0
                                color = (0,0,255)
                        elif 0<= per_val2 <=10 and dir1 == 0:
                                count5+=0.5
                                dir1 = 1
                                color = (0,0,255)
                        else:
                                color =(0,0,225)

                        

                        print(int(count4))
                        print(int(count5))

                        write_data("count4.txt", count4)
                        write_data("count5.txt", count5)
                        
                    
                        cv2.rectangle(frame,(580,int(bar_val2)),(0+620,300+60),color,cv2.FILLED)
                        cv2.rectangle(frame,(580,100),(0+620,300+60),(255,255,255),1)
                        cvzone.putTextRect(frame,f"{int(per_val2)} %",(560,400),1.2,1,(255,255,255),color,border=1,colorB=())
                        cvzone.putTextRect(frame,'Squat Exercise',(40,40),1.5,2,(255,255,255),(255,0,0),border=2,colorB=())
                        cvzone.putTextRect(frame,f'count4 : {int(count4)}',(40,80),1.5,2,(0,0,0),(0,255,255),border=2,colorB=())
                        cvzone.putTextRect(frame,f'count5 : {int(count5)}',(40,120),1.5,2,(0,0,0),(0,255,255),border=2,colorB=())
        FRAME_WINDOW.image(frame) 
result_count = read_data("count.txt")
result_count1 = read_data("count1.txt")
result_count2 = read_data("count2.txt")
result_count3 = read_data("count3.txt")
result_count4 = read_data("count4.txt")
result_count5 = read_data("count5.txt")


msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
body1 = "Tổng số lần tập tay trái: " + str(int(float(result_count)))
body2= "Số lần tập tay trái đúng : " + str(int(float(result_count1)))
body3 = "Tổng số lần tập tay phải: " + str(int(float(result_count2)))
body4= "Số lần tập tay phải đúng: " + str(int(float(result_count3)))
body5= "Tổng số lần tập chân: "  + str(int(float(result_count4)))
body6= "Số lần tập chân đúng: "   + str(int(float(result_count5)))
  

msg_body = body1 + "\n" + body2 + "\n" + body3 + "\n" + body4 + "\n" + body5 + "\n" + body6
msg.attach(MIMEText(msg_body, "plain"))

result = read_data("checkrun.txt") 
if result =="run":
        try:
                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                        server.starttls()
                        server.login(sender_email, sender_password)
                        text = msg.as_string()
                        server.sendmail(sender_email, receiver_email, text)
                        print("Đã gửi email thành công!")
        except Exception as e:
                print("Gửi email thất bại. Lỗi: ", e)
cap.release()
cv2.destroyAllWindows() 

