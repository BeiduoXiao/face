#coding:utf-8
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import wx 



#"选择一张图片"按钮的点击事件
def printcoords():
    
    #File就是所选图片的路径
    global File 
    File = filedialog.askopenfilename(parent=root, initialdir="C:/",title='Choose an image.')
    #print File
    image=Image.open(File)
    image=image.resize((300,400))
    filename = ImageTk.PhotoImage(image)
    canvas.image = filename  
    canvas.create_image(0,0,anchor='nw',image=filename)


#“测试”按钮的点击事件
def test():
    
    import main
    import radar
    #新窗口
    root = Toplevel()
    root.geometry('1280x600')
    root.title("检测结果")
    #分区域的季节类型结果展示画布
    cv_parts = Canvas(root, bg = 'white', width = 640, height = 480) 
    cv_parts.grid(row=0, column=0)
    
    #计算
    result=main.main(File)
    #解析结果集并绘图
    radar.radar_part(result[0],result[1],result[2],result[3])
    
    radar_part_im=Image.open("radar_part.png")
    radar_part_im=radar_part_im.resize((640,480))
    filename = ImageTk.PhotoImage(radar_part_im)
    cv_parts.image = filename
    cv_parts.create_image(0,0,anchor='nw',image=filename)

    
    
    #综合结果展示画布
    cv_total = Canvas(root, bg = 'white', width = 640, height = 480) 
    cv_total.grid(row=0, column=1)

    #解析结果集并绘图
    radar.radar_total(result[4])
    
    radar_total_im=Image.open("radar_total.png")
    radar_total_im=radar_total_im.resize((640,480))
    filename = ImageTk.PhotoImage(radar_total_im)
    cv_total.image = filename
    cv_total.create_image(0,0,anchor='nw',image=filename)

    #文字区域
    season=result[5]
    lb=Label(root, text='您所属的季节类型是：',font=('Arial', 30))
    lb.grid(row=1,column=0,sticky="e")
    lb=Label(root, text=season,font=('Arial', 30))
    lb.grid(row=1,column=1,sticky="nw")
    root.mainloop()


if __name__ == "__main__":
    #主窗口
    root = Tk()
    root.geometry('500x500')
    root.title("“四季型人”自动检测")
    canvas= Canvas(root, bg = 'white', width = 300, height = 400)
    canvas.pack()
    Button(root,text='选择一张照片',command=printcoords).pack()
    Button(root,text='测试季节类型',command=test).pack()
    root.mainloop()

