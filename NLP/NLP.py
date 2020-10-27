import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import urllib.request
import plotly.io as pio

# reading a page
page =  urllib.request.urlopen('https://en.wikipedia.org/wiki/Natural_language_processing')
html_pain = page.read()
#print(html_pain)

# data cleaning
soup = BeautifulSoup(html_pain,'html.parser')
soup_text = soup.get_text(strip = True)
ready_text = soup_text.lower()
#print(ready_text)

# Tokenisation
tokens = []
for t in ready_text.split():
    tokens.append(t)

#print(tokens)
stop_words = stopwords.words('english')
clean_tokens = tokens[:]

for token in tokens:
    if token in stop_words:
        clean_tokens.remove(token)

#print(clean_tokens)

# Data Visualisation
freq = nltk.FreqDist(clean_tokens)

#for key, val in freq.items():
#    print('Word: ' + str(key) + '. Quantity: ' + str(val))

high_freq = dict()
for key, val in freq.items():
    if (val > 10):
        high_freq[key]= val

fig = dict({
    "data": [{"type": "bar",
              "x": list(high_freq.keys()),
              "y": list(high_freq.values())}],
    "layout": {"title": {"text": "Most frequently used words in the page"}, "xaxis": {"categoryorder":"total descending"}}
})
pio.show(fig)