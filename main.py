#!/usr/bin/env python -W ignore::DeprecationWarning
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:17:06 2019

chatbot corpus comes from:
https://github.com/gunthercox/chatterbot-corpus

@author: whq672437089
"""
import logging
from chatbot.logger_util import get_logger
from generateResponse import generateResponse, porterStemmerInput
from preprocess import pureQuestionsText, generateSentenceTokens, generateConversationTurnDict, sanitize_questions
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)

logger = get_logger(logging.INFO)

# read file with lower into content
content = ""
with open("corpus.txt") as infile:
    for line in infile:
        content = content + " " + line.lower()

# qrDict is dict: {
#                   sanitized_question1: [answer1, answer2],
#                   sanitized_question2: [answer3, answer4]
#               }
qrDict = generateConversationTurnDict(content)


# a text of sanitized_questions
pureQuestions = pureQuestionsText(qrDict)
# a list of tokenized_sentence
sentenceTokens = generateSentenceTokens(pureQuestions)

# for index map of senitized_question to tokenized_question
ql = []
for question, response in qrDict.items():
    ql.append(question)
logger.debug(ql)

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
            sentenceTokens.remove(porterStemmerInput(userInput))
    else:
        flag = False
        print("ROBO: Bye! take care..")
