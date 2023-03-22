# urllib.request
from urllib.request import urlopen 
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

my_site='https://www.airnow.gov/?city=Monterey&state=CA&country=USA'

site_html=urlopen(my_site)

# print out a portion of the HTML
print(site_html.read()[5000:5400].decode('utf-8'))

# # beautifulsoup
# # create BeautifulSoup object
from bs4 import BeautifulSoup

soup = BeautifulSoup(site_html.read(), 'lxml')

print(soup.title)

# just the text of the title
print(soup.title.text)

# find all images
# can replace 'img' with other html tags
images = soup.findAll('img')

# loop through list of images and retrieve 'src' attribute
for image in images:
   print(image['src'])

# #scraping airnow.gov
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# my_site='https://www.airnow.gov/?city=Monterey&state=CA&country=USA'

# site_html=urlopen(my_site)
# soup = BeautifulSoup(site_html.read(), 'lxml')

# aqi_div = soup.find('div', {'class': 'aqi'})
# print(aqi_div)