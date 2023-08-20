# in this session we perform data scrapping on the web of jobs.ps
import requests as req
from bs4 import BeautifulSoup as bs

url = "https://www.jobs.ps/jobs/procurement-officer-49723"
# url = "http: " can connect to local host (https for web in the browser)

try:
    response = req.get(url)

    # it's of type response
    print(type(response))

    # Status Code 200
    print(response.status_code)

    soup = bs(response.content, 'html.parser')

    headings = soup.select('div.view--content--heading')
    content = soup.select('div.view--content--desc')
   
    for div in headings:
        print(div.text) # this outputs the div codes actually
    # print(len(content)) returns 3
    print(content[0])

    jobDescription = ""
    for span in content[0].find_all('span'):
        jobDescription += span.text # to access each span content
    
    print(jobDescription)
except: 
    print("Error!")

# and then we crerate a virtual environmnet using pipreqs, 
## I have encountered an error with windows, abdallah advices to install Linux