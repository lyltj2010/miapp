# coding:utf-8
from bs4 import BeautifulSoup

class HtmlParser(object):

    def parse_urls(self,response):
        pass

    

    def parse_app_details(self,response):
        # how to handle exception?
        item = {}
        soup = BeautifulSoup(response.text)
        # intro titles section
        intro = soup.find('div', {"class":"intro-titles"})
        item["name"] = intro.h3.get_text()
        item["company"] = intro.findAll("p")[0].get_text()
        item["category"] = intro.findAll("p")[1].findAll('b')[0].next_sibling
        item["support"] = intro.findAll("p")[1].findAll('b')[1].next_sibling
        item["rating"] = intro.div.div['class']
        item["comments_num"] = intro.find("span",{"class":"app-intro-comment"}).get_text()

        # ul class=" cf" section
        ul = soup.find("ul",{"class":" cf"}).children
        for i, li in enumerate(ul):
            if i == 1:
                item["size"] = li.get_text()
            if i == 3:
                item["version"] = li.get_text()
            if i == 5:
                item["updated_at"] = li.get_text()

        item["root"] = soup.find("ul",{"class":"second-ul"}).get_text()
        item["url"] = response.url

        return item