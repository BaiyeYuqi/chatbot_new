# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 16:50:30 2019

@author: whq672437089
"""

# the idea behind how this chatbot response is "document similarity", as this chatbot will
# measure how user input question is similar to the processed corpus questions.
import string
import nltk
import re

nltk.download('punkt')
nltk.download('wordnet')


def generateConversationTurnDict(inputText):
    # split text to independent conversation turn by usinig '--'
    conversationTurn = re.split(r'-\s+-', inputText)
    # remove empty string in the string list
    conversationTurnWithoutEmpty = list(filter(lambda x: len(x)>1, conversationTurn)) 
    
    qrDict={}
    for turn in conversationTurnWithoutEmpty:
        # divide turn into question and answers
        # first part is question as key,second part is response as value
        subparts=re.split(r'\s+-', turn)
        if(len(subparts)==2):
            sub1=subparts[0].rstrip().lstrip()
            qrDict[sub1]=subparts[1].rstrip()
    return qrDict


def pureQuestionsText(qrDict):
    questions=""
    # extract questions and combine them into one text
    for question, response in qrDict.items():
        question=sanitize_questions(question)
        questions=questions+question+' .\n '
    return questions


def generateSentenceTokens(questions):
    import nltk
    sentences = nltk.sent_tokenize(questions)
    return sentences


def sanitize_questions(question):
    sanitized_question = question.translate(str.maketrans('', '', string.punctuation)).rstrip().lstrip()
    return sanitized_question



   
