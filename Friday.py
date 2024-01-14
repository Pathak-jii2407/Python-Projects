import datetime
import os
import random
import winsound
import time
import webbrowser
from tkinter import messagebox
import speech_recognition as sr
import tkinter as tk
import pyautogui
import pyttsx3
import pyautogui as pg
import cv2
import face_recognition


root=tk.Tk()
root.title('\U0001F916')
root.max_width = 170
root.max_height = 50

root.minsize(100, 30)

root.maxsize(root.max_width, root.max_height)


root.after_cancel=False
root.attributes("-topmost", True)

root.attributes("-toolwindow",True)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


hour = int(datetime.datetime.now().hour)
minute = int(datetime.datetime.now().minute)
day = int(datetime.datetime.now().day)
month = int(datetime.datetime.now().month)


def date():
    speak(f'Today is {day} {month}th month')
    speak(f'{hour} hour{minute}minute')

def factorial(factorial_num):
    if factorial_num == 1:
        return 1
    else:
        return factorial_num *  factorial(factorial_num-1)
    
def wishMe():  
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! ", )

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
def get(self):
        """Return the text."""
        return self.tk.call(self._w, 'get')



def play_notification_beep():
    frequency = 1000  
    duration = 1000  
    winsound.Beep(frequency, duration)


def sleep():
    time.sleep(60)
def shut_down():
    speak("going to sleep in 5 seconds")
    t = 5
    speak(t)
    while True:
        t = (int(t) - 1)
        speak(t)
        if (t == 0):
            break
        goodBye()
        pyautogui.hotkey('alt', 'w')
        os.system("shutdown /l")

def goodBye():
        speak("Welcome sir, I'm Always with you bloody")
        play_notification_beep()
        exit()

def restart():
    t = 5
    speak(t)
    while(t!=0):
        t = (int(t) - 1)
        speak(t)
    goodBye()
    pyautogui.hotkey('alt', 'f4')
    os.system("shutdown /r /t 1")
def instagrm():
    webbrowser.open("https://www.instagram.com/pathak_jii2407/")
def exit_loop():
    play_notification_beep()
    exit()

def youtubeplay(que):
    try:
        web = "https://www.youtube.com/results?search_query=" + que
        webbrowser.open_new(web)
        
        speak("Done sir") 
    except Exception as e:
        print(f"An error occurred: {e}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        label=tk.Label(root,text=f'you said: {query}\n')
        label.pack(side='right')

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

date()
speak("Please wait Untill I recognize you")


def arvis():
    speak("Yes Boss")
    try:
        for i in range(10):
            query = takeCommand().lower()
            if query=='YouTube':
                query='youtube'
            if query=="Friday":
                query="friday"  
            
            
            elif 'friday' in query:
                friday={
                    "query":["Yes boss","I woke up","Sorry sir, I was Sleeping",
                            "I am Lisning","What can I do for You","Present Boss"]
                    }
                friday_choose=int(random.randint(0,6))
                speak(friday["query"][friday_choose])


            elif 'intro' in query:
                speak('I am Artificial Intelligence')
                speak("invented by ved prakash pathak ")
            


            elif 'command prompt' in query:
                speak("opening command prompt")
                os.system("start cmd")

            elif 'WhatsApp' in query:
                path = 'https://web.whatsapp.com/'
                webbrowser.open_new(path)

            elif 'google' in query:
                speak("searching on google...")
                query = query.replace("on google", '')
                webb = "https://www.google.com/search?q=" + query
                webbrowser.open(webb)
                speak("I found this")

            elif 'shutdown' in query:
                shut_down()

            elif 'restart' in query:
                restart()

            elif "shut down" in query:
                shut_down()

            elif 'close' in query:
                speak("closing the running app")
                pyautogui.hotkey('alt', 'f4')

                
            elif 'close all' in query:
                speak("closing all tab")
                pyautogui.hotkey('ctrl', 'shift', 'w')
                
            elif 'calculate' in query:
                quer=query.replace('calculate','')
                que=quer.replace('x','*')
                qu=que.replace('into','*')
                calci_=f"the answer is: {eval(qu)}"
                speak(calci_)
                answer_label = tk.Label(root,text=f"answer:{calci_}\n")
                answer_label.pack(side='right')
                answer_label.destroy()

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")


            elif 'remember that' in query:
                rememberMsg = query.replace("remember that", "")
                rememberMsg = rememberMsg.replace("Jarvis", "")
                speak("you tell me to Remind me That :" + rememberMsg)
                remember = open('data.txt', 'w')
                remember.write(rememberMsg)
                remember.close()

            elif 'tell you' in query:
                remember = open('data.txt', 'r')
                speak("you tell me that " + remember.read())
            elif 'factorial of' in query:
                factorial_num=query.replace('factorial of','')
                speak(f"The factorial of {factorial_num} is {factorial(int(factorial_num))}")

            elif 'countdown of' in query:
                if "minute" in query:
                    que=query.replace('start','')
                    qu=que.replace('countdown of','')
                    q=qu.replace('minute','')
                    min = int(q) * 60
                    timer_alert=min-5

                    for remaining_time in range(min):
                        min-=1
                        if min<=6:
                            speak(min)
                        if min==timer_alert:
                            speak('I will remind you soon')
                        if min>=timer_alert:
                            speak(min)
                        time.sleep(0.90)
                    play_notification_beep()
                else:
                    que=query.replace('start','')
                    qu=que.replace('countdown of','')
                    q=qu.replace('minute','')
                    speak(qu)
                    
                    for x in range(int(qu)):
                            time.sleep(1)
                            speak(qu)
                            qu-=1
                    play_notification_beep()
            elif 'youtube'in query:                        
                speak("playing...")
                que=query.replace('on YouTube','')
                youtubeplay(que)

            elif "abuse" in query:
                quer=query.replace('abuse','')
                que=quer.lower()
                if que=='ved':
                    speak("I do not use Abusing words")
                for i in range(5):
                    name=f"youu {que}"
                    speak(name)
                    play_notification_beep()
            elif "write" in query:
                quer=query.replace('write',"")
                speak("Please open NotePad")
                time.sleep(10)
                pg.write(quer)
            
                
            elif 'thanks' in  query:
                goodBye()
            elif 'exit' in  query:
                goodBye()


    except Exception as e:
        messagebox.showerror('Error',[speak("Somthing went wrong with connection"),
                                      "Somthing went wrong with connection"])





def face():
    known_faces = {
        "Boss": face_recognition.load_image_file("E:\\FRIDAY\\pics\\1.jpg"),     
        "Saksham Singh": face_recognition.load_image_file("E:\\FRIDAY\\pics\\saksham.jpg"),     
    }

    known_encodings = {}

    for name, img in known_faces.items():
        face_encoding_list = face_recognition.face_encodings(img)
        if face_encoding_list:
            known_encodings[name] = face_encoding_list[0]
        else:
            print(f"No face found in the image for {name}")

    video_capture = cv2.VideoCapture(0)
    unknown_face_count=10

    while True:
        ret, frame = video_capture.read()

        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for current_face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(list(known_encodings.values()), current_face_encoding)

            name = "unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = list(known_encodings.keys())[first_match_index]
                speak(f"Welcome {name}")
                

                def button_clicked():
                    jarvis_.config(text="Listining...",bg="#FFA500", relief=tk.SUNKEN)

                def button_released():
                    jarvis_.config(text="<FRIDAY\U0001F916>",bg="#FFD700", relief=tk.RAISED)


                try:
                    jarvis_ = tk.Button(root, text="<FRIDAY\U0001F916>",bg="#FFD700",font='bold',border=3,borderwidth=3,highlightbackground='black',highlightthickness=5,highlightcolor='red',command=arvis)
                    jarvis_.bind("<Button-1>", lambda event: button_clicked())
                    jarvis_.bind("<ButtonRelease-1>", lambda event: button_released())
                    jarvis_.pack()


                except Exception as e:
                    speak("Somthing went wrong with connection")
                    messagebox.showerror("Error",e)
                    
                tk.mainloop()

            
            else:
                print(unknown_face_count)
                if unknown_face_count>7:
                    speak(f"you have {unknown_face_count} attempts")
                if unknown_face_count<=7:
                        speak({unknown_face_count})
                if unknown_face_count==0:
                    play_notification_beep()
                    exit()

            unknown_face_count=unknown_face_count-1


            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        # cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

face()




