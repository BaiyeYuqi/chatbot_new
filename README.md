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

### Assignment 3 Feature Introduction:
* A simple gui for user to typing which make the conversation more clear to see

 ![Image text](https://github.com/BaiyeYuqi/chatbot_new/blob/Gui-and-sockets-finished/img/1553550117(1).jpg)
 
* Add extra topic about detail of sports which make user have more topics to talk about

 ![Image text](https://github.com/BaiyeYuqi/chatbot_new/blob/Gui-and-sockets-finished/img/1553551392(1).jpg)
 
 * Add the feature that can handle spelling mistakes which makes the conversation more smooth
 
  ![Image text](https://github.com/BaiyeYuqi/chatbot_new/blob/Gui-and-sockets-finished/img/1553551440(1).jpg)
  
  * use one of the language toolkits to improve the correctness of matching, which is WordNetLemmatize that can restore word trunk, and  use the cosine_similarity tool to match the best similarity question, also use the Tfidvecrorizer to classify the question
  
  ![Image text](https://github.com/BaiyeYuqi/chatbot_new/blob/Gui-and-sockets-finished/img/1553551518(1).jpg)
  
   * use of sockets so this chatbot can communicate with other agent if the HOST and PORT is the same 
   
   ![Image text](https://github.com/BaiyeYuqi/chatbot_new/blob/Gui-and-sockets-finished/img/1553551665(1).jpg)
### How to use this program:
* Open spyder or anything can run python file
* Open two console
* First run server.py in first console
* Second run client.py in second console
* type you question in the client gui appears and click send
* than you will receive answer with question recorded on server gui



