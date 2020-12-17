from bs4 import BeautifulSoup
import requests

def scraper(url):
    req = requests.get(url)
    cnt = req.content
    soup = BeautifulSoup(cnt, 'html.parser')
    th_ = soup.findAll('th')
    td_ = soup.findAll('td')

    th_lst = [item.get_text()for item in th_][2:-1]
    td_content = [item.get_text() for item in td_][2:]
    td_content.pop(108)

    new_lst = []
    for item in range(0, len(td_content),11):
        new_lst.append(td_content[item:item+10])
    
    
    return new_lst

