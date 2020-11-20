# Election Tweets Text Analysis by Nick Yohn  
  # Analyze word frequency
  # Analyze frequency of hashtags
  # Compare Biden mentions vs. Trump mentions

# Tweets were randomly selected from Top 50 Latest on Twitter under '#Election 2020' on November 13th, 2020

import matplotlib.pyplot as plt

stopwords = ['the','of','and','','be','have','he','to','or','in','by','a','for','as','I','it','this','is','are','so','you','on','that','no','but','my','not','can','will','feels','with','when','&','has','about','As','up',]


def get_lines(file):
  with open(file) as text:
    tweets = []
    for lines in text:
      tweets.append(lines)
  return tweets
      
def get_words(text):  
  global words
  words = []
  for line in text:
    for word in line.split():
      if word not in stopwords:   
        words.append(word.lower())   
  return words

def get_hashtags(words): 
  hashtags = []
  for word in words:
    if word.startswith('#') == True:
      hashtags.append(word)
  return hashtags

def get_biden_count(words):  # includes both words and hashtags
  biden_count = []  
  for word in words:
    if word == "biden": 
      biden_count.append(word)
    elif word == "#bidenharris2020":
      biden_count.append(word)
    elif word == "#biden":
      biden_count.append(word)
    elif word == "#joebiden":
      biden_count.append(word)
    elif word == "@joebiden":
      biden_count.append(word)
  return biden_count

def get_trump_count(words):  
  trump_count = []  
  for word in words:
    if word == "trump": 
      trump_count.append(word)
    elif word == "#trump":
      trump_count.append(word)
    elif word == "#donaldtrump":
      trump_count.append(word)
    elif word == "@realdonaldtrump":
      trump_count.append(word)
  return trump_count

def get_freqs(group):  # 'group' can be words/hashtags
  global freqs
  freqs = {}
  for word in group:
    if word in freqs:
      freqs[word] += 1
    else:
      freqs[word] = 1
  return freqs

def get_data(freqs,number): 
  sorted_dict = sorted(freqs.items(),key = lambda x:x[1],reverse=True)
  x = [v[0] for v in sorted_dict[:number]]
  y = [v[1] for v in sorted_dict[:number]]  
  return x,y

def create_bar_graph(x,y):  # vertical bar graph
  plt.bar(x,y, color = [(0.57, 0, 0), (0.63, 0, 0),(0.74, 0, 0),(0.86, 0.1, 0.1),(0.98, 0.4, 0.4),(0.99, 0.6, 0.6),(0.99, 0.8, 0.8),(0.99, 0.95, 0.95)]) # red RGB
  plt.xlabel('Words')
  plt.ylabel('Frequency')
  plt.title('Most Common Election-Related Words',loc='center')
  plt.show()

def create_barh_graph(x,y):  # horizontal bar graph
  plt.barh(x,y, color = [(0.09, 0.24, 0.74),(0.17, 0.35, 0.81),(0.25, 0.48, 0.92),(0.41, 0.56, 0.96),(0.53, 0.67, 0.97),(0.64, 0.75,0.99)]) # blue RGB
  plt.subplots_adjust(left = 0.28, bottom = None, right = None, top = None, wspace = None, hspace = None)
  plt.xlabel('Hashtags')
  plt.ylabel('Frequency')
  plt.title('Most Common Election-Related Hashtags',loc='center')
  plt.show()

def create_pie_chart(biden,trump): # pie chart
  biden_pct = (len(biden)/(len(trump)+len(biden))) 
  trump_pct = ((len(trump))/(len(trump)+len(biden)))
  sizes = [biden_pct, trump_pct]
  labels = 'Biden', 'Trump'
  plt.pie(sizes, labels = labels, autopct = '%1.1f%%', startangle = 90, shadow = True, colors = ['blue','red'])
  plt.title('Biden vs. Trump Twitter Mentions (n=47)',loc='center')
  plt.show()