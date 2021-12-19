urls = []
urls.append("https://collegedunia.com/sivaganga-colleges")

state = "Tamil Nadu"

no_of_pagedowns = 100


from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd

for u in urls:  
    save_name = u[25:]+'.csv'     
    save_name = save_name.replace("/","-")      
    options = webdriver.ChromeOptions()         
    options.add_argument('headless')
    options.add_argument('window-size=1200x600')   ome
    browser = webdriver.Chrome(chrome_options=options)  
    browser.get(u)                             
    time.sleep(1)                             
    elem = browser.find_element_by_tag_name("body")    
    while no_of_pagedowns:                      
        elem.send_keys(Keys.PAGE_DOWN)         
        time.sleep(0.4)                         
        no_of_pagedowns-=1                     

    df = pd.DataFrame(columns=['S No','College Name', 'Course Name','Fees','Eligibilty'])
    html = browser.page_source           
    main_page_content = BeautifulSoup(html)     
    browser.close()                     
    Content = []                            
    for i in range(len(main_page_content.find_all("div", {"class": "clg-name-address"}))):
        paragraphs = main_page_content.find_all("div", {"class": "clg-name-address"})[i]
        link=url= paragraphs.a['href']          
        name = paragraphs.text                      
        Content.append(paragraphs.text)           
        link = url                                
        response = requests.get(link, timeout=10) 
        page_content = BeautifulSoup(response.content, "html.parser")  
        textContent = []                          
   
        for k in range(len(page_content.find_all("div",{"class": "address row"}))):
            paragraphs_new = page_content.find_all("div",{"class": "address row"})[k].text
            textContent.append(paragraphs_new)

        #Prints the name of the colleges
        #Create a list to store the detais and finally dumps into there Pandas dataframe
        print(name)
        list=[]
        list.append(i+1)
        list.append(name)
        list.append(course)
        list.append(fees)
        list.append(eligibility)
        #it dumps it here
        df.loc[i+1]=list
        #pandas dumps it to the specified csv file from here.
        df.to_csv(r'~/Desktop/'+save_name,index=None,encoding='utf-8')
