import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
from .models import Mail


def generate_words(url):
    if Mail.objects.filter(url=url).exists():
        mail_object = Mail.objects.get(url=url)
        words = mail_object.words
    else:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        text = ' '.join(s.get_text(strip=True) for s in soup.find_all('p'))
        words_count = Counter(word.strip(punctuation).lower()
                              for word in text.split())
        words = words_count.most_common()
        Mail.objects.create(url=url, words=words)
    return words
