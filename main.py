# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:17:06 2019

chatbot corpus comes from:
https://github.com/gunthercox/chatterbot-corpus

@author: whq672437089
"""
from generateResponse import generateResponse
from preprocess import pureQuestionsText, generateSentenceTokens, generateConversationTurnDict, sanitize_questions

content = ""
with open("corpus.txt") as infile:
    for line in infile:
        content = content + " " + line.lower()

qrDict = generateConversationTurnDict(content)
for index, (question, answer) in enumerate(qrDict.items()):
    print("question is:"+question+', answer is:'+answer+', index is:'+str(index))
    pass

pureQuestions = pureQuestionsText(qrDict)
sentenceTokens = generateSentenceTokens(pureQuestions)
for index, question in enumerate(sentenceTokens):
    # print("index is:"+str(index)+", question is:"+question)
    pass

ql = []
for question, response in qrDict.items():
    ql.append(question)
print (ql)

flag = True
print("ROBO: Hello, I am a chatbot. Type Bye to exit")

while flag:
    userInput = input()
    userInput = sanitize_questions(userInput.lower())
    if userInput != 'bye':
        if userInput in ['thanks', 'thank you']:
            flag = False
            print("ROBO: You are welcome..")
        else:
            print("ROBO: "+ generateResponse(userInput, sentenceTokens, qrDict, ql))
            sentenceTokens.remove(userInput)
    else:
        flag = False
        print("ROBO: Bye! take care..")
    