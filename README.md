# 310 Assignment 3

### Author: 

Yuqi Sun

### Introduction: 

This is a simple chatbot program. The most fundamental theory that this program relies on is text similarity. 

The following steps decribe the logic of this program:
* Clean text, including remove punctuation, duplicate whitespace.
* Divide text into multiple independent conversaiton turns.
* Based on such conversation turns, create a dictionary whose key is the question and value is the response.
* Combine only questions, then tokenlizing and lemmatization them.
* Vectorize those sentence tokens and compare the user input with them.
* Find the most similar question and use it as key to retrieve answer from training corpus.
* Output answer/response.

The training corpus used in our project comes from this [Repo](https://github.com/gunthercox/chatterbot-corpus)

### How to use this program:
* Open spyder or anything can run python file
* Open two console
* First run server.py in first console
* Second run client.py in second console
* type you question in the client gui appears and click send
* than you will receive answer with question recorded on server gui



