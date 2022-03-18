from cProfile import label
from tempfile import template
import tkinter
from task1 import useTemplateAnalyze
from task2 import useCascadeAnalyze
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from PIL import Image, ImageTk

templates = {
    'face': 'template1',
    'small face': 'template2',
    'eyes_nose': 'template3',
    'eyes': 'template4',
    'left eye': 'template4a',
    'right eye': 'template4b',
    'mouth': 'template5',
    'nose': 'template6',
}




class GUI:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Task 1")
        self.window.geometry('600x600')
        

    def start(self):
        self.window.mainloop()

    def open_file(self):
        global img, file_path
        my_str = tkinter.StringVar()
        l2 = tkinter.Label(self.window,textvariable=my_str,fg='red' )
        l2.pack()
        my_str.set("")
        file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*jpg')])
        if file_path is not None:
            img=Image.open(file_path)
            width, height = img.size  
            width_new=int(width/3)
            height_new=int(height/3)
            img_resized=img.resize((width_new,height_new))
            img=ImageTk.PhotoImage(img_resized)
            my_str.set(file_path)
            b2 = Button(self.window,image=img)
            b2.pack()
            
    
    def addTemplateButton(self, templateName):
        style = tkinter.ttk.Style()
        style.configure("TButton", background='#96c0eb')
        btn = tkinter.ttk.Button(self.window, text=templateName, style="TButton", command=lambda: useTemplateAnalyze(templates[templateName], file_path))
        btn.pack()
    def uploadButton(self):
        my_font1=('times', 18, 'bold')
     
        face = Label(self.window, text='Upload Face in jpg format ', anchor=CENTER, width=30,font=my_font1 )
        face.pack()
        facebtn = Button(self.window, text ='Choose File', width=20, command = lambda: gui.open_file()) 
        facebtn.pack()
        label1 = Label(self.window, text='Template Matching', anchor=CENTER, width=30,font=my_font1 )
        label1.pack()
    def addCascadeButton(self):
        my_font1=('times', 18, 'bold')
        label2 = Label(self.window, text='Viola-Jones method', anchor=CENTER, width=30,font=my_font1 )
        label2.pack()
        style = tkinter.ttk.Style()
        style.configure("TButton", background='#96c0eb')
        btn = tkinter.ttk.Button(self.window, text='Viola-Jones method', style="TButton", command=lambda: useCascadeAnalyze(file_path))
        btn.pack()
        
    
gui = GUI()

gui.uploadButton()

gui.addTemplateButton('face')
gui.addTemplateButton('small face')
gui.addTemplateButton('eyes_nose')
gui.addTemplateButton('eyes')
gui.addTemplateButton('left eye')
gui.addTemplateButton('right eye')
gui.addTemplateButton('mouth')
gui.addTemplateButton('nose')

gui.addCascadeButton()

gui.start()
    