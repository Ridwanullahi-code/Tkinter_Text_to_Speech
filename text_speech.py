from tkinter import*
from tkinter import ttk
from PIL import ImageTk,Image 
import pyttsx3


def Convert_button():
	engine = pyttsx3.init()
	e1 = text2.get(1.0,END)

	voices = engine.getProperty("voices")
	combo_val = combo.get()

	if combo_val == "MALE":
		engine.setProperty("voice",voices[0].id)
		engine.say(e1)
		engine.runAndWait()

	else:
		engine.setProperty("voice", voices[1].id)
		engine.say(e1)
		engine.runAndWait()

def clear_button():
	text2.delete(1.0,END)


def Text_Speech():
	Display_root()
	Display_title()
	Display_speech()
	Display_text()
	Display_button()
	root.mainloop()

def Display_root():

	global root,arrow_logo,speaker_logo,pause_logo,combo_val
	root = Tk()
	root.geometry("835x468+335+172")
	root.title("Music App")
	root.resizable(width=NO,height=NO)
	root.config(bg="#F7F7F7")
	arrow_logo = ImageTk.PhotoImage(Image.open("arrow.png"))
	speaker_logo = ImageTk.PhotoImage(Image.open("speaker.png"))
	
def Display_title():
	title = Label(root,text="TEXT-SPEECH CONVERTER",bd=5,bg="white",font=("Roboto",25,"bold"),relief=GROOVE)
	title.place(x=0,y=0,width=835)

def Display_speech():
	global combo
	arrow = Label(root,image=arrow_logo)
	arrow.place(x=390,y=170)

	label = Label(root,text="TEXT",bd=5,bg="white",font=("Roboto",25,"bold"),relief=GROOVE)
	label.place(x=70,y=70,width=200)
	speaker = Label(root,image = speaker_logo)
	speaker.place(x=650,y=130)

	sec_lb = Label(root,text="CHANGE VOICE:",bg="#F7F7F7",font=("times new roman",12,"bold"))
	sec_lb.place(x=600,y=300)
	combo = ttk.Combobox(root,font=("Roboto",11,"bold"),values=("MALE","FEMALE"))
	combo.set("MALE")
	combo.place(x=740,y=300,width=80)

def Display_text():
	global text2
	label = Label(root,text="SPEECH",bd=5,bg="white",font=("Roboto",25,"bold"),relief=GROOVE)
	label.place(x=600,y=70,width=200)
	text_frame = Frame(root,bg="white")
	text_frame.place(x=20,y=132,width=320,height=200)

	scrollbar = Scrollbar(text_frame,orient=VERTICAL)
	scrollbar.pack(side=RIGHT,fill="y")
	text2 = Text(text_frame,bg="white",font=("Roboto",15,"bold"),yscrollcommand=scrollbar.set)
	text2.pack(side=LEFT)
	scrollbar.configure(command=text2.yview)
	
def Display_button():
	convt = Button(root,text="CONVERT",fg="white",bg='#B200ED',font=("Roboto",15,"bold"),command=Convert_button)
	convt.place(x=390,y=280,width=160)
	clear = Button(root,text="CLEAR",fg="white",bg='red',font=("Roboto",15,"bold"),command=clear_button)
	clear.place(x=350,y=410,width=170)
	
print(Text_Speech())