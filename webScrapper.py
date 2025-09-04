import requests
from bs4 import BeautifulSoup
import csv
import json
from datetime import datetime


def scrape_quotes():

    url = "http://quotes.toscrape.com/"

    response = requests.get(url)


    soup = BeautifulSoup(response.text, 'html.parser')


    quotes = soup.find_all('div', class_='quote')

    
    quotes_list = []

    for quote in quotes:

        text = quote.find('span', class_='text').text


        author = quote.find('small', class_='author').text
        
        tags = [tags.text for tag in quote.find_all('a', class_='tag')]


        quotes_list.append({
            'text': text,
            'author': author,
            'tags': ', '.join(tags)
        })

        print(f"Author: {author}")
        print(f"Quote: {text}")
        print(f"Tags: {', '.join(tags)}")
        print("-" * 50)

    return quotes_list    

if __name__ == "__main__":
    quotes = scrape_quotes()
    print(f"\n Scraped {len(quotes)} quotes!")