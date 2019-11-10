import requests
import pandas as pd 
from bs4 import BeautifulSoup

source = requests.get("https://www.monsterindia.com/search/results?sort=1&limit=100&query=Data%20Science&locations=india&searchId=ed0adc96-11b5-4b26-a703-12708679d043")
soup = BeautifulSoup(source.text,'html.parser')


containers = soup.find_all('div',{'class':'card-body card-body-apply pd10'}) 
print(len(containers))


df = pd.DataFrame(columns=["Title","Location","Company","Skills"])

for container in containers:
    try:
        title = container.find('h3',{'class':'medium'}).text.replace('\n','').strip()
    except:
        title = 'None'
    try:
        location = container.find('span',{'class':'loc'}).text.replace('\n','').strip()
    except:
        location = 'None'
    try:
        company = container.find('span',{'class':'company-name'}).text.replace('\n','').strip()
    except:
        company = 'None'
    try:
        skills = container.find('p',{'class':'descrip-skills'}).text.replace(',','*').replace('\n','').strip()
    except:
        skills = 'None'
        
    df = df.append({'Title':title,'Location':location,"Company":company,"Skills":skills},ignore_index=True)
    

df.to_csv('datascience.csv',index=False)
            
        
        
    



