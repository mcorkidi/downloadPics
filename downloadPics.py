# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 17:17:02 2019

@author: Corkidi
"""

import re
import requests
from bs4 import BeautifulSoup

site = 'http://images.boardriders.com/global/billabong-products/all/default/hi-res'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]


for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative 
            # if it is provide the base url which also happens 
            # to be the site variable atm. 
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)