import requests
import re
import csv
import pandas as pd

from pages.quotes_page import QuotesPage

all_url = []
for i in range(1,11):
    a = f'https://quotes.toscrape.com/page/{i}/'
    
    all_url.append(a)

quotes_library = []

for i in all_url:
    page_content = requests.get(i).content
    
    page = QuotesPage(page_content)
    quotes_library.append(page.quotes)

# page_content = requests.get('https://quotes.toscrape.com').content

# page = QuotesPage(page_content)

all_quotes = [item for sublist in quotes_library for item in sublist]

quotes_pattern = '“(.*?)”'
author_pattern = '(”\sby\s)(.*?)>'

quotes = []
author = []

for quote in all_quotes:
    q = re.search(quotes_pattern, str(quote)).group(1)
    a = re.search(author_pattern, str(quote)).group(2)
    
    quotes.append(q)
    author.append(a)

key_val_quotes = dict(zip(quotes, author))

# with open('Quote.csv', 'w', newline='') as csvfile:
#     columns = ['Quote', 'Author']
#     writer = csv.DictWriter(csvfile, fieldnames=columns)
    
#     writer.writeheader()
#     for key in key_val_quotes:
#         writer.writerow({'Quote': key, 'Author': key_val_quotes[key]})

df = pd.DataFrame(key_val_quotes.items(), columns=['Quote', 'Author'])

df.to_csv('All_quotes.csv', index = False)
