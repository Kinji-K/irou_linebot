from bs4 import BeautifulSoup
import requests

class GetUpdate:
    def __init__(self):
        self.url = "https://iro-doku.com/"
        self.line = []

    def CheckUpdate(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.text, 'html.parser')

        articles = soup.select('article')
        for article in articles:
            self.line.append({
                "id": article['id'].split("-")[1],
                "title": article.select_one('h3').get_text(),
            })
        
        return self.line

if __name__ == "__main__":
    data = GetUpdate()
    print(data.CheckUpdate())