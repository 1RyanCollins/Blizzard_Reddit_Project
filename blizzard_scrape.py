#blizzard test

import praw
import pandas as pd
import datetime as dt
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from textblob import Blobber
from collections import Counter 

reddit = praw.Reddit(client_id='0STBJJrrTH53SA', 
                     client_secret='7ttL7PpTdf6CrjfFiJJz4xJdQlg', 
                     user_agent='Social_Media_Mining_Project', 
                     username='NicCage4life', 
                     password='Texasfans131')


submission = reddit.submission(url='https://www.reddit.com/r/Blizzard/comments/e96zkd/im_going_to_have_this_feeling_of_inadequacy/')
submission = reddit.submission(id='e96zkd')

sublist = []
submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    sublist.append(comment.body)

#with open('blizzard40.txt', mode='wt', encoding='utf-8') as myfile:
 #       myfile.write('\n'.join(sublist))



#new_list= []

#for w in sublist:
#	testimonial= TextBlob(w)
#	testimonial.sentiment
#	new_list.append(testimonial.sentiment.polarity) #-1 bad , #1 good 
#	print(sum(new_list)/len(new_list)) #average

#test = ["I fucking hate you" + "I really hate you so much" + "Ban blizzard"]

blobber = Blobber(analyzer = NaiveBayesAnalyzer())
for sentences in sublist:
    sentences = sentences.encode('unicode-escape').decode('utf-8')
    blob = blobber(sentences)
    result = [blob.sentiment.classification]
    print(result)

neg = []
pos = []
for sentences in sublist:
    sentences = sentences.encode('unicode-escape').decode('utf-8')
    blob = blobber(sentences)
    result = [blob.sentiment.classification]
    for items in result:
        if items == 'neg':
            neg.append(items)
        if items == 'pos':
            pos.append(items)

print(len(neg) / len(pos + neg))
            
        







    
    




 

  
