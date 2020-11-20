import analysis

file_name = 'tweets.py'

# depending on which functions you run, you can analyze word frequency, hashtags frequency, or Biden/Trump twitter mentions

def main():
  tweets = analysis.get_lines(file_name)
  words = analysis.get_words(tweets)
  
  # tags = analysis.get_hashtags(words)
  biden_count = analysis.get_biden_count(words)
  trump_count = analysis.get_trump_count(words)
  
  # freqs = analysis.get_freqs(words)
  # x,y = analysis.get_data(freqs,6)
  # for word in freqs:
    # print(word,":",freqs[word])

  # analysis.create_bar_graph(x,y)
  # analysis.create_barh_graph(x,y)
  analysis.create_pie_chart(biden_count,trump_count)

main()