

import requests 
from bs4 import BeautifulSoup 
import csv

class Allbeautifulsoap:
    def __init__(self,Http):
         self.Http=Http
    #Extracting text from all paragraphs
    def TextURL(self): 
            # Making a GET request 
            r = requests.get(self.Http) 
    
            # Parsing the HTML 
            soup = BeautifulSoup(r.content, 'html.parser') 
    
            s = soup.find('div', class_='entry-content') 
    
            lines = s.find_all('p') 
    
            for line in lines: 
                text = print(line.text)
            return text

    #Extracting links
    def UrlsOnly(self):
        # Making a GET request 
        r = requests.get(self.Http) 
    
        # Parsing the HTML 
        soup = BeautifulSoup(r.content, 'html.parser') 
    
        # find all the anchor tags with "href"  
        for link in soup.find_all('a'): 
            text=print(link.get('href'))
        return text

    #Extracting images from a web site

    def ImagesInURL(self):
        # Making a GET request 
        r = requests.get(self.Http) 
    
        # Parsing the HTML 
        soup = BeautifulSoup(r.content, 'html.parser') 
    
        images_list = [] 
    
        images = soup.select('img') 
        for image in images: 
            src = image.get('src') 
            alt = image.get('alt') 
            images_list.append({"src": src, "alt": alt}) 
        
        for image in images_list: 
            images = print(image)
        return images

    #Saving data to csv
    def SavingToCSV(self,filename):
        req= requests.get(self.Http)
  
        soup = BeautifulSoup(req.text, 'html.parser') 
  
        titles = soup.find_all('div', attrs={'class', 'head'}) 
        titles_list = [] 
    
        count = 1
        for title in titles: 
            d = {} 
            d['Title Number'] = f'Title {count}'
            d['Title Name'] = title.text 
            count += 1
            titles_list.append(d) 
  
        filename = filename
        with open(filename, 'w', newline='') as f: 
            w = csv.DictWriter(f,['Title Number','Title Name']) 
            w.writeheader() 
            w.writerows(titles_list)
        


