# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 00:21:47 2020

@author: Tanumay Misra
"""

from info_retrieval import extract_single_line_tfidf
import streamlit as st
import spacy
nlp1 =spacy.load("en_core_web_sm")

import stanza
nlp2 = stanza.Pipeline('en')
#from flask import Flask, render_template, request
#app = Flask(__name__)
#
#@app.route('/')
#def student():
#   return render_template('student.html')
#
#@app.route('/result',methods = ['POST', 'GET'])
#def result():
#   if request.method == 'POST':
#      result = request.form
#      #extract_single_line_tfidf()
#      context = result.get('Context')
#      question = result.get('Question') 
#      response = extract_single_line_tfidf(context,question)
#      result = {'Context':context,'Question': question,'result': response}
#      return render_template("result.html",result = result)
#   
#
#if __name__ == '__main__':
#   app.run(debug = True)
   

def main():
    
    st.title('Information Retrieval From Text')
    html_temp = """<p style="color:green">retrieve information using NER!!!.</p>"""
    st.markdown(html_temp,unsafe_allow_html = True)
    
    #st.write('Put Yout Text Here!!!')
    context = st.text_area('Put Yout Text Here!!!','type here')
    
    text = st.sidebar.title("CHOSE YOUR OPTION!!")
    
    model_name = st.sidebar.selectbox('select model',('spacy','stanza'))
    entity_name = st.sidebar.selectbox('select entity',('organization','location'))
    
    logo = st.sidebar.image("images/nlp.png")
    
    
    def get_entity(entity_name):
        if model_name == 'spacy':
            doc = nlp1(context)
            response = ""
            if entity_name == 'organization':
                for ent in doc.ents:
                    if ent.label_ == 'ORG':
                        response += ent.text+'||'
            if entity_name == 'location':
                for ent in doc.ents:
                    if ent.label_ == 'GPE':
                        response += ent.text+'||'
#            if entity_name == 'money':
#                for ent in doc.ents:
#                    if ent.label_ == 'MONEY':
#                        response += ent.text+'||'
            return response
                        
        else:
            doc = nlp2(context)
            response = ""
            if entity_name == 'organization':
                for sent in doc.sentences:
                    for token in sent.ents:
                        if token.type == 'ORG':
                            response += token.text+'||'
                            
            if entity_name == 'location':
                for sent in doc.sentences:
                    for token in sent.ents:
                        if token.type == 'LOC':
                            response += token.text+'||'
                            
#            if entity_name == 'MONEY':
#                for sent in doc.sentences:
#                    for token in sent.ents:
#                        if token.type == 'MONEY':
#                            response += token.text+'||'
                            
            return response
                            
            
        
    if st.button('Extract_entity'):
        st.write('Entity ::',get_entity(entity_name))
            

if __name__=='__main__':
    main()
        

