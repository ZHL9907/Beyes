import cv2
from matplotlib import pyplot as plt
import tkinter as tk
import tkinter.filedialog as file
import tkinter.messagebox as mes
import jieba
import numpy as np
import docx
from tkinter import scrolledtext as st

def OpenDoc():
    global words
    filename = file.askopenfilename(title='打开文件名字', initialdir="Bayes",
                                    filetypes=[('docx文件', '*.docx')])
    doc1=docx.Document(filename)
    fullText=[]
    for para in doc1.paragraphs:
        print(para.text)
        fullText.append(para.text)
    print("len",len(fullText))
    ft=np.array(fullText)
    cft=''
    bd = ',!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+。，！？“”《》：、． '

    for i in range(len(ft)):
         cft=cft+ft[i]
    for i in bd:
        cft = cft.replace(i,'')
    words= jieba.lcut(cft)  #通过jieba分开句子变成词语，用cft格式分开（这里用空格）
    std.delete(1.0,tk.END)  #删除之前的数据
    std.insert(tk.END, words)
    return


OpenDoc()