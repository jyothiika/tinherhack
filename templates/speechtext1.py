#!/usr/bin/env python
# coding: utf-8

# In[22]:


import speech_recognition as sr


# In[23]:


a=sr.Recognizer()


# In[24]:


with sr.Microphone() as source:
    print("Say something")
    audio=a.listen(source)
    try:
        text = a.recognize_google(audio)
        print("you Said :{}".format(text))
        
    except:
        print("Sorry could not recognize")

