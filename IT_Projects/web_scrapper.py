import requests as rq
from bs4 import BeautifulSoup as bs
import os

# Website with inspirational images
url = ("https://www.google.com")

# Download page for parsing
page = rq.get(url)
src = page.content
soup = bs(src, 'html-parser')

# locate all elements with image tag
image_tags = soup.find_all('img')

# create directory for inspirational images
if not os.path.exists('quotes'):
    os.makedirs('quotes')

# move to new dir
os.chdir('quotes')

# image file name variable
x = 0

# writing imaages
for image in image_tags:
    try:
        url = image['src']
        source = rq.get(url)
        if source.status_code == 200:
            print(url)
            pass
            with open('quote-' + str(x) + '.jpg', 'w') as f:
                f.write(rq.get(url).content)
                f.close()
                print('Done ' + x)
                x += 1
    except:
        print("Didn't execute")
