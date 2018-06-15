#Question 1
'''
import re

pattern = r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})'
print(re.findall(pattern,  "zuck26@facebook.com" "page33@google.com"
"jeff42@amazon.com",flags=re.IGNORECASE))


#Question 2
import re
print(re.findall(r'\bB\w+', "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better.", flags=re.IGNORECASE))


#Question 3
import re
print(" ".join(re.split('[;,\s_]+', "A, very   very; irregular_sentence")))


#Question 4
import re
def clean_tweet(tweet):
    tweet = re.sub('http\S+\s*', '', tweet)
    tweet = re.sub('RT|cc', '', tweet)
    tweet = re.sub('#\S+', '', tweet)
    tweet = re.sub('@\S+', '', tweet)
    tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)
    tweet = re.sub('\s+', ' ', tweet)
    return tweet

print(clean_tweet('Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'))
'''