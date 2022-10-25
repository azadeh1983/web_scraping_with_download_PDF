
import requests
from bs4 import BeautifulSoup

URL = 'https://www.hindawi.com/journals/apec/2018/3408480/'

download_urls = []

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content,"html.parser") # make our page easy to navigate
soup2=soup.find_all('a',class_='ButtonGroup_buttonGroupWrapper__LPDDG')

for a in soup2: # iterate through every <a> tag on the page
  href = a['href'] # get the href attribute of the tag
  if href[-4:] == '.pdf': # if the link ends  .pdf
    downloadLink =  href # create the download url
    download_urls.append(downloadLink) # add the link to our array
#
for file in download_urls: # for each index and file in download_urls
  fileName = file.split('/')[-1] # the text after the last / is the file name we want
  fileRequest = requests.get(file) # download the file
  with open(fileName, 'wb') as examFile: # open a new file in write and binary mode
    examFile.write(fileRequest.content) # write the content of the downloaded file
print('download successfully with this name:'+fileName)