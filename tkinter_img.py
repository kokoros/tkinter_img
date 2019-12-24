#! /usr/bin/env python3
# coding=utf-8

'''
进行GUI编程
'''

import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
#导入opencv
import cv2

class TkinterImg(object):
    def __init__(self):
        self.width = 700
        self.height = 700

        self.size = (700, 500)

        #默认图片路径
        self.file_path = "a1.jpg"
        self.block_size = 7
        self.constant_value = 3



    def main_window(self):
        '''主窗口'''
        self.window = tk.Tk()

        self.window.title("img_to_threshold")
        #设置几何图形划分
        self.window.geometry("{}x{}".format(self.width, self.height))

    def get_file_path(self):
        '''获取文件绝对路径'''
        file_path = askopenfilename()
        print(file_path)
        self.file_path = file_path

        try:
            img = Image.open(file_path)
            # 略缩图片
            img.thumbnail(self.size, Image.ANTIALIAS)
            #转为tk识别的格式
            tk_img = ImageTk.PhotoImage(image=img)

            #改变img_label
            self.img_label['image'] = tk_img

            self.window.mainloop()

        except OSError:
            print('please choose one picture!')

    def get_blocksize_value(self, value):
        '''
        获取blocksize滑动块的值
        :return:
        '''
        blocksize_list = [i for i in range(3, 100, 2)]
        #value就是索引
        # print(value)
        block_size = blocksize_list[int(value)]
        print(block_size)
        self.block_size = int(block_size)


    def get_constant_value(self, value):
        '''
        获取常数c的值
        :param value:
        :return:
        '''
        print(value)
        self.constant_value = int(value)



    def show_img(self):
        '''
        展示选择的图片
        :return:
        '''
        # frame_img = tk.Frame(self.frame_father, width=300, height=500, bg="yellow")
        # frame_img.pack(side=tk.LEFT)

        #打开图片
        img = Image.open("a1.jpg")
        #略缩图片
        img.thumbnail(self.size, Image.ANTIALIAS)
        # image = img.resize(self.width, self.height, Image.ANTIALIAS)
        # print(image)

        tk_img = ImageTk.PhotoImage(image=img)
        # print(tk_img)
        #在frame_img中添加img_label
        self.img_label = tk.Label(self.window, text="aaa", image=tk_img)
        # print(img_label)
        # img_label['image'] = tk_img
        # img_label.image = tk_img

        #显示img_label
        self.img_label.grid(row=0, sticky=tk.W)


        #显示选择文件的按钮
        file_button = tk.Button(self.window, text="choose picture", command=self.get_file_path)
        file_button.grid(row=1, sticky=tk.E)

        #显示blocksize的滑动条
        self.blocksize_scale = tk.Scale(self.window,
                                   #标签
                                   label="blocksize",
                                   from_=0,
                                   #终止值
                                   to=48,
                                   # tickinterval=2,
                                   #步距
                                   resolution=1,
                                   length=400,
                                   #横向
                                   orient=tk.HORIZONTAL,
                                   #回调函数
                                   command=self.get_blocksize_value,
                                  )
        #设置blocksize滑动条的默认值
        self.blocksize_scale.set(7)
        self.blocksize_scale.grid(row=2, sticky=tk.W)

        #显示blocksize的滑动条
        self.constant_scale = tk.Scale(self.window,
                                   #标签
                                   label="constant",
                                   #终止值
                                   to=10,
                                   # tickinterval=2,
                                   #步距
                                   resolution=1,
                                   length=200,
                                   #横向
                                   orient=tk.HORIZONTAL,
                                   #回调函数
                                   command=self.get_constant_value,
                                  )

        self.constant_scale.set(3)
        self.constant_scale.grid(row=2, sticky=tk.E)

        #增加二值化按钮
        file_button = tk.Button(self.window, text="img_to_threshold", command=self.img_to_threshold)
        file_button.grid(row=3, sticky=tk.E)


        # 显示窗口
        self.window.mainloop()

    def img_to_threshold(self):
        '''
        把图片二值化
        :return:
        '''
        img_view = cv2.imread(self.file_path, cv2.IMREAD_GRAYSCALE)
        # ret, imgviewx2 = cv2.threshold(img_view, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        # adaptiveThreshold 自适应阈值
        new_img_view = cv2.adaptiveThreshold(img_view, 200, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, self.block_size, self.constant_value)

        #保存图片
        cv2.imwrite('test.jpg', new_img_view)

        #显示图片
        img = Image.open('test.jpg')
        # 略缩图片
        img.thumbnail(self.size, Image.ANTIALIAS)
        # 转为tk识别的格式
        tk_img = ImageTk.PhotoImage(image=img)

        # 改变img_label
        self.img_label['image'] = tk_img
        self.window.mainloop()




    def run(self):
        self.main_window()
        #显示图片
        self.show_img()









if __name__ == "__main__":
    tkinter_img = TkinterImg()
    tkinter_img.run()
