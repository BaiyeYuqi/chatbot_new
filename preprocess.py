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
import logging

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

logger = logging.getLogger(__name__)

def generateConversationTurnDict(inputText):
    # split text to independent conversation turn by usinig '--'
    conversationTurn = re.split(r'-\s+-', inputText)
    # remove empty string in the string list
    conversationTurnWithoutEmpty = list(filter(lambda x: len(x)>1, conversationTurn)) 
    
    qrDict={}
    for turn in conversationTurnWithoutEmpty:
        # divide turn into question and answers
        # first part is question as key,second part is response as value
        subparts = re.split(r'\s+-', turn)
        question = subparts[0].strip()
        question = sanitize_questions(question)
        answers = [_.strip() for _ in subparts[1:]]
        qrDict[question] = answers
    logger.debug(qrDict)
    return qrDict


def pureQuestionsText(qrDict):
    questions = ""
    # extract questions and combine them into one text
    for question, response in qrDict.items():
        questions += question + ' .\n '
    logger.debug(questions)
    return questions


def pos_tag_sentence(sentence):
    tokens = nltk.word_tokenize(sentence)
    tokens_new = nltk.pos_tag(tokens)
    tokens_new = [_[0] for _ in tokens_new]
    logger.debug(tokens_new)
    return ' '.join(tokens_new)


def generateSentenceTokens(questions):
    import nltk
    sentences = nltk.sent_tokenize(questions)
    logger.debug(sentences)
    sentences = [pos_tag_sentence(_) for _ in sentences]
    return sentences


def sanitize_questions(question):
    """ Clean extra punctuations, white space and newlines"""
    sanitized_question = question.translate(str.maketrans('', '', string.punctuation)).strip()
    return sanitized_question
