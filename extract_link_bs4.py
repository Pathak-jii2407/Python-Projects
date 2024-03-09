import requests
from bs4 import BeautifulSoup
from csv import writer


def Searching(url,subject):
    response=requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.find('title').get_text().replace('/',',')
    print(title)
    with open(f'{title}', 'w', newline='', encoding='utf-8') as file:
        csv_writer=writer(file)
        headers=['sr.','link','Text']
        csv_writer.writerow(headers)
        links=soup.find_all('a')
        
        for i, link in enumerate(links, start=1):
            main=link.get('href','')
            doc=link.get_text(strip=True).replace(' ','').lower()
            csv_writer.writerow([i,main,doc])
            if subject in doc:
                print(main)

    
        
url=input('Enter Link:')
subject=input('What You are searching')

Searching(url,subject)
