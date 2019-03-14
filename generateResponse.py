# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:03:35 2019

@author: whq672437089
"""
import random

from nltk import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from nltk.stem import WordNetLemmatizer
import logging

from preprocess import generateSentenceTokens
logger = logging.getLogger(__name__)


def lemTokens(tokens):
    """for a given sentence,return a lemmatized sentence"""
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]

def porterStemmerInput(input):
    logger.debug(input)
    tokens = generateSentenceTokens(input)
    ps = PorterStemmer()
    pstokens = [ps.stem(w) for w in tokens]
    userInput = ' '.join(pstokens)
    logger.debug(userInput)
    return userInput


def generateResponse(userInput, sentences, askResponseDict, ql, similarityThredhold=0.7):
    # prevent bad input
    if similarityThredhold > 1 or similarityThredhold < 0:
        similarityThredhold = 0.5

    logger.info(userInput)
    sentences.append(porterStemmerInput(userInput))

    # vetorize sentences and userinput for fllowing similarity calculation
    TfidfVec = TfidfVectorizer(tokenizer=lemTokens, stop_words='english')
    vertorizedSentences = TfidfVec.fit_transform(sentences)
    vals = cosine_similarity(vertorizedSentences[-1], vertorizedSentences)

    # find index of sentences that has highest similarity with input
    valsWithoutLast = vals[0, :-1]
    idx = np.argmax(valsWithoutLast, axis=0)

    # return response
    if vals[0][idx] < similarityThredhold:
        robotResponse="Your input keywords donot exist in my knowledge"
        return robotResponse
    else:
        question = ql[idx]
        print("matched question from database: " + question)
        answers = askResponseDict.get(question)
        robotResponse = '' + random.choice(answers)
        return robotResponse