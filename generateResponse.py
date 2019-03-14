# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:03:35 2019

@author: whq672437089
"""
import random

from nltk import PorterStemmer
from nltk.corpus import wordnet
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from nltk.stem import WordNetLemmatizer
import logging

from preprocess import generateSentenceTokens
logger = logging.getLogger(__name__)


def synoTokens(tokens):
    def syno_anto_token(token):
        from nltk.corpus import wordnet
        synonyms = []
        antonyms = []
        for syn in wordnet.synsets(token):
            for l in syn.lemmas():
                synonyms.append(l.name())
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
        logger.debug(set(synonyms))
        logger.debug(set(antonyms))
        if synonyms:
            return synonyms[0]
            # return random.choice(synonyms)
        return token
    return [syno_anto_token(token) for token in tokens]


def lemTokens(tokens):
    """for a given sentence,return a lemmatized sentence"""
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]


def stemTokens(tokens):
    def porterStemmerToken(token):
        ps = PorterStemmer()
        return ps.stem(token)
    return [porterStemmerToken(token) for token in tokens]


def generateResponse(userInput, sentences, askResponseDict, ql, similarityThredhold=0.7):
    # prevent bad input
    if similarityThredhold > 1 or similarityThredhold < 0:
        similarityThredhold = 0.5

    sentences.append(userInput)

    # vetorize sentences and userinput for fllowing similarity calculation
    TfidfVec = TfidfVectorizer(tokenizer=stemTokens, stop_words='english')
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