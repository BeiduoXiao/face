#coding:utf-8
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import wx 

if __name__ == "__main__":
    root = Tk()
    root.geometry('300x300')
    canvas= Canvas(root, bg = 'red', width = 99, height = 99)
    canvas.pack()
    #setting up a tkinter canvas with scrollbars
    #frame = Frame(root, bd=2, relief=SUNKEN)
    #frame.grid_rowconfigure(0, weight=1)
    #frame.grid_columnconfigure(0, weight=1)
    #xscroll = Scrollbar(frame, orient=HORIZONTAL)
    #xscroll.grid(row=1, column=0, sticky=E+W)
    #yscroll = Scrollbar(frame)
    #yscroll.grid(row=0, column=1, sticky=N+S)
    #canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    #canvas.grid(row=0, column=0, sticky=N+S+E+W)
    #xscroll.config(command=canvas.xview)
    #yscroll.config(command=canvas.yview)
    #frame.pack(fill=BOTH,expand=1)


    #function to be called when mouse is clicked
    def printcoords():
        #File就是所选图片的路径
        File = filedialog.askopenfilename(parent=root, initialdir="C:/",title='Choose an image.')
        #print File
        image=Image.open(File)
        image=image.resize((100,100))
        filename = ImageTk.PhotoImage(image)
        canvas.image = filename  # <--- keep reference of your image
        canvas.create_image(0,0,anchor='nw',image=filename)
    
    def test():
    
 
        root = Tk()
        root.geometry('300x300')
        cv = Canvas(root, bg = 'red', width = 100, height = 100) 
        cv.grid(row=0, column=0)
        cv2 = Canvas(root, bg = 'red', width = 100, height = 100) 
        cv2.grid(row=0, column=1)
        cv3 = Canvas(root, bg = 'red', width = 100, height = 100) 
        cv3.grid(row=1, column=0)
        cv4 = Canvas(root, bg = 'red', width = 100, height = 100) 
        cv4.grid(row=1, column=1)
        lb=Label(root, text='Hello, world!')
        lb.grid(row=0, column=4)
        root.mainloop()
    
    Button(root,text='选择一张图片',command=printcoords).pack()
    Button(root,text='测试',command=test).pack()
    root.mainloop()

