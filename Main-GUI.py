#MADE BY SIDTHEMINER
#Twitter @SidTheMiner
#Youtube SIDTHEMINER 
#Hope you like the project
# I am a beginner so forgive me if I made some mistakes.
#Have a good day :)


####MODULES IMPORT####

from tkinter import *
from tkinter import ttk
from gtts import gTTS
from playsound import playsound
from PIL import Image, ImageTk 
import random
import string
import shutil
from tkinter import messagebox 

###########MAIN WINDOW#################


#Screen
screen=Tk()
screen.title("Text To Speech converter")
screen.geometry("1100x650")
screen.configure(background='#232323')
screen.resizable(width=False, height=False)
screen.iconbitmap(r"Images\icon.ico")

####VARIABLES####

Text_get=StringVar()
Selected_speed=StringVar()

###########################FUNCTIONS########################################


#For File name lenght

len=random.randrange(3,10)

####MAIN FUNCTION#####

def Text_to_speech():

    if Selected_speed.get()=='Fast':
        try:
            Main_text = Text_get.get()
            speech = gTTS(text = Main_text, lang='en', slow=False)
            filename=''.join(random.choices(string.ascii_letters+string.digits,k=len))  
            speech.save(filename +'.mp3')  
            playsound(filename +'.mp3')

            shutil.move(filename +'.mp3', "Converted-Audio")

           
        except:
            messagebox.showinfo("Error","Error! Click reset and try again")  

    else:
        try:
            Main_text = Text_get.get()
            speech = gTTS(text = Main_text, lang='en', slow=True)  
            filename=''.join(random.choices(string.ascii_letters+string.digits,k=len))
            speech.save(filename +'.mp3')  
            playsound(filename +'.mp3') 

            shutil.move(filename +'.mp3', "Converted-Audio")

        except:
            messagebox.showinfo("Error","Error! Click reset and try again")  


#####RESET FUNCTION#####

def Reset():
    Text_get.set("")

####PLAY BUTTON HOVER ANIMATION####

def on_enter_play(e):
   Play_btn.config(image=Play_btn_render1, bd=0,bg='#161616',activebackground="#161616",background='#232323')


def on_leave_play(e):
   Play_btn.config(image=Play_btn_render, bd=0,bg='#161616',activebackground="#161616",background='#232323')


####RESET BUTTON HOVER ANIMATION#### 


def on_enter_Reset(e):
   Reset_btn.config(image=Reset_btn_render1, bd=0,bg='#161616',activebackground="#161616",background='#232323')


def on_leave_Reset(e):
   Reset_btn.config(image=Reset_btn_render, bd=0,bg='#161616',activebackground="#161616",background='#232323')
    

########################WINDOW SETUP##################################


#Background
BG_load= Image.open(r"Images\BGimage.png")
BG_render = ImageTk.PhotoImage(BG_load)

#Background image display
img = Label(screen, image=BG_render,background='#232323')
img.place(x="0",y="0")


#frame1
frame1 = Frame(screen,bg="#EC4D37")
frame1.place(x=75,y=200)

#frame2
frame2 = Frame(frame1,bg="#1D1B1B",width=950,height=300)
frame2.pack(pady=0.5,padx=0.5)


#paste image load
Text_load= Image.open(r"Images\button_text.png")
Text_render = ImageTk.PhotoImage(Text_load)

#paste image display
img1 = Label(screen, image=Text_render,background='#232323',bd=0)
img1.place(x="100",y="250")

####Text ENTRY####
Text=Entry(screen,textvariable=Text_get,font="Arial 15",fg="#EC4D37",bg="#232323", ).place(x=175,y=256,width=700,height=34)

#Speed Image load
Speed_load= Image.open(r"Images\button_select-speed.png")
Speed_render = ImageTk.PhotoImage(Speed_load)

#Speed Image display
img2 = Label(screen, image=Speed_render,background='#232323',bd=0)
img2.place(x="100",y="300")

#Speed Combo box
Speed=('Fast','Slow')
Speed_CB=ttk.Combobox(screen, textvariable=Selected_speed)
Speed_CB['values']=Speed
Speed_CB['state'] = 'readonly'
Speed_CB.current(0)
Speed_CB.place(x=250,y=307,width=280,height=30)


#info image load
info_load= Image.open(r"Images\info.png")
info_render = ImageTk.PhotoImage(info_load)

#Info image display
img123 = Label(screen, image=info_render,background='#232323')
img123.place(x="540",y="309")

####PLAY BUTTON####


#Button Image2 load
Play_btn_load1= Image.open(r"Images\button_play (2).png")
Play_btn_render1 = ImageTk.PhotoImage(Play_btn_load1)

#Button Image1 load
Play_btn_load= Image.open(r"Images\button_play.png")
Play_btn_render = ImageTk.PhotoImage(Play_btn_load)

#Button
Play_btn = Button(screen, image=Play_btn_render, bd=0,bg='#161616',activebackground="#161616",background='#161616',command=Text_to_speech)
Play_btn.place(x=450,y=390)

#Bind
Play_btn.bind('<Enter>', on_enter_play)
Play_btn.bind('<Leave>', on_leave_play)


####Reset BUTTON####


#Reset Button Image 2 load
Reset_btn_load1= Image.open(r"Images\button_reset (1).png")
Reset_btn_render1 = ImageTk.PhotoImage(Reset_btn_load1)

#Reser Button image 1 load

Reset_btn_load= Image.open(r"Images\button_reset.png")
Reset_btn_render = ImageTk.PhotoImage(Reset_btn_load)

#Button
Reset_btn = Button(screen, image=Reset_btn_render, bd=0,bg='#161616',activebackground="#161616",background='#232323',command=Reset)
Reset_btn.place(x=885,y=255)

#Bind
Reset_btn.bind('<Enter>', on_enter_Reset)
Reset_btn.bind('<Leave>', on_leave_Reset)


####LOOP####
screen.mainloop()

#HOPE YOU LIKED IT :)