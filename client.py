# -*- coding: utf-8 -*-
"""
Created on Wed March 19 15:03:35 2019

@author: whq672437089
"""

import threading
import tkinter
from socket import *
from tkinter import *
import time
from tkinter.scrolledtext import ScrolledText

global socket_connect, dialog_box, send_box


def send_message():
    sendData = send_box.get()
    if sendData == 'bye':
        dialog_box.insert(tkinter.END, "You have disconnected from the server. See you again!!!" + "\n")
        dialog_box.see(tkinter.END)
        socket_connect.sendall(bytes(sendData, encoding="utf8"))
        socket_connect.close()
    else:
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        dialog_box.insert(tkinter.END, "[" + now + "] client:" + sendData + "\n")
        dialog_box.see(tkinter.END)
        socket_connect.sendall(bytes(sendData, encoding="utf8"))
    send_box.delete(0, END)


# get response
def receive_data():
    while True:
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        accept_data = str(socket_connect.recv(1024), encoding="utf8")
        dialog_box.insert(tkinter.END, "[" + now + "] server:" + accept_data + "\n")
        dialog_box.see(tkinter.END)


if __name__ == "__main__":
    # initial the gui
    root = tkinter.Tk()
    # set the title of gui
    root.title("Chatbot client")
    # set tips
    frame1 = Frame(root)
    frame1.pack()
    IP_Show_Label = Label(frame1, text="Hello, I am a chatbot. Type Bye to exit.\n")
    IP_Show_Label.pack(side='left')

    # dialog
    frame2 = Frame(root)
    frame2.pack()
    dialog_box = ScrolledText(frame2, width=70, height=15)
    dialog_box.bind("<KeyPress>", lambda e: "break")
    dialog_box.pack(side="bottom", fill='both', expand=True)

    # send button
    frame3 = Frame(root)
    frame3.pack()
    e3 = StringVar()
    send_box = Entry(frame3, textvariable=e3, width=60)
    buttontext2 = tkinter.StringVar()
    buttontext2.set('Send')
    button_Send = tkinter.Button(frame3, width=10, textvariable=buttontext2, command=send_message)
    send_box.pack(side="left")
    button_Send.pack(side="left")
    frame3.pack()

    # init
    HOST = '127.0.0.1'
    PORT = 5000
    ADDR = (HOST, PORT)
    socket_connect = socket(AF_INET, SOCK_STREAM, 0)
    socket_connect.connect(ADDR)
    thread = threading.Thread(target=receive_data)
    thread.start()

    root.mainloop()