from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import requests
from func.Txt_summarize_helper import Summarize

class News_set(object):
    
    def __init__(self):
        self.BBC_url = 'https://www.bbc.com/news'
        self.BBC_url_save = []
        self.BBC_add_save = []
        self.Summarizing = Summarize()

    def get_BBC_news(self):
        self.BBC_url_save = []
        response = requests.get(self.BBC_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        counter = 0
        content = ""
        for h in soup.find('body').find_all('a', { 'class': 'gs-c-promo-heading' }):
            url_conf = ""
            # news_title = h.contents[0].lower
            if(counter == 0): 
                counter += 1
                continue
            if(counter < 6):
                content += h.text
                content += '\n'
                url_conf += 'https://www.bbc.com'
                url_conf += h['href']
                content += 'https://www.bbc.com'
                content += h['href']
                content += '\n'
                counter += 1
                self.BBC_url_save.append(url_conf)
            else: break
        return content

    def Get_summarize(self, index):
        try:
            content = ''
            target_url = self.BBC_url_save[index]
            response = requests.get(target_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            count = 0
            for h in soup.find('body').find_all('p', { 'class': 'ssrcss-1q0x1qg-Paragraph' }):
                if count > 0: break
                content += h.text
                count += 1
            return content
        except Exception:
            print("Value Error or no url")
            return ""

    def add_save(self, index):
        try:
            self.BBC_add_save.append(self.BBC_url_save[index - 1])
            content = "Success saving "
            content += self.BBC_add_save[index - 1]
            return content
        except Exception:
            print("Value error")
            return ""

    def watch_save(self):
        content = ""
        counter = 1
        for save_url in self.BBC_add_save:
            content += str(counter)
            content += '. ' 
            content += save_url
            content += '\n'
            counter += 1
        return content

    def del_save(self, index):
        if index == -1:
            self.BBC_add_save = []
            return "All Clear"
        else:
            self.BBC_add_save.pop(index - 1)
            return f"Success Clear index of {index}"