# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 23:50:11 2020

@author: Tanumay Misra
"""
import nltk
import string

from nltk.corpus import stopwords 
from nltk.tokenize import sent_tokenize 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#stop_words = set(stopwords.words('english')) 

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

def extract_single_line_tfidf(input_string,question):
    sent_tokens = sent_tokenize(input_string)
    sent_tokens.append(question)
    
    tfidfVec = TfidfVectorizer(tokenizer = LemNormalize,stop_words = 'english')
    tfidf = tfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    
    if(req_tfidf==0):
        robo_response= "I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = sent_tokens[idx]
        return robo_response
    
    
    