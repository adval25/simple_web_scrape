from bs4 import BeautifulSoup
import requests

page = requests.get('http://quotes.toscrape.com')
soup = BeautifulSoup(page.text, 'html.parser')
quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

if __name__ == '__main__':
    upper_bound = min(len(quotes), len(authors))
    for i in range(upper_bound):
        print(quotes[i].text + ' - ' + authors[i].text)
