
# -*- coding: utf-8 -*-
"""
Created on Wed March 19 15:03:35 2019

@author: whq672437089
"""

import socket
import time
from tkinter.scrolledtext import ScrolledText
import threading
import tkinter
from tkinter import *
from generateResponse import generateResponse
from preprocess import *

global dialog_box, send_box


def init_reponse_paramters():
    content = ""
    with open("corpus.txt") as infile:
        for line in infile:
            content = content + " " + line.lower()
    qrDict = generateConversationTurnDict(content)
    pureQuestions = pureQuestionsText(qrDict)
    sentenceTokens = generateSentenceTokens(pureQuestions)
    ql = []
    for question, response in qrDict.items():
        ql.append(question)
    return qrDict, sentenceTokens, ql


def server_thread(sock, caddr):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    dialog_box.insert(tkinter.END, "[" + now + "] client@" + str(caddr[1]) + "conneted!\n")
    
    while True:
        # receive data
        data = str(sock.recv(1024).decode('UTF-8'))
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if data == "bye":
            dialog_box.insert(tkinter.END, "[" + now + "] client@" + str(caddr[1]) + "close the dialog.\n")
            dialog_box.see(tkinter.END)
            break
        else:
            dialog_box.insert(tkinter.END, "[" + now + "] client@" + str(caddr[1]) +":"+ data + '\n')
            dialog_box.see(tkinter.END)
        # send message
        time.sleep(0.2)
        qrDict, sentenceTokens, ql = init_reponse_paramters()
        userInput = sanitize_questions(data.lower())
        data = generateResponse(userInput, sentenceTokens, qrDict, ql)
        sock.sendall(bytes(data, 'UTF-8'))
    sock.close()


# listen the socket connect
def server_accept(ss):
    while True:
        sock, caddr = ss.accept()
        Thread2 = threading.Thread(target=server_thread, args=(sock, caddr))
        Thread2.start()


# init the server
def server_Init():
    HOST = '0.0.0.0'
    PORT = 5000
    ADDR = (HOST, PORT)
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.bind(ADDR)
    ss.listen(20)
    Thread1 = threading.Thread(target=server_accept, args=(ss,))
    Thread1.daemon = True

    Thread1.start()

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("chatbot server")
    frame2 = Frame(root)
    frame2.pack()
    dialog_box = ScrolledText(frame2, width=100, height=30)
    dialog_box.bind("<KeyPress>", lambda e: "break")
    dialog_box.pack(side="bottom", fill='both', expand=True)
    server_Init()
    root.mainloop()

