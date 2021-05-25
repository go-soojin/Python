#!/usr/bin/env python
# coding: utf-8

# In[19]:


# 라이브러리 선언 
import pandas as pd 
from bs4 import BeautifulSoup 
from selenium import webdriver
import requests, bs4

# 웹 브라우저 설정 
options = webdriver.ChromeOptions() 
options.add_argument("window-size=1920*1080")
driverLoc = "C:/Users/SMART-07/Desktop/addon/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=driverLoc, options = options) 
driver.implicitly_wait(3)

# 브라우저 열기
targetUrl = "https://www.daisomall.co.kr"
driver.get(targetUrl)


# In[20]:


# 브라우저 내 액션(텍스트 입력 및 검색)
from selenium.webdriver.common.keys import Keys
daisoSearchXpath = '/html/body/div/div/div[1]/div[3]/div/div/div[2]/form/div/dl/dt/input' 
daisoSearchBox = driver.find_element_by_xpath(daisoSearchXpath)
searchKeyword = "캠핑의자"
daisoSearchBox.send_keys(searchKeyword)
daisoSearchBox.send_keys(Keys.ENTER)

# 페이지 Url 및 소스 가져오기
finalUrl = driver.current_url
pgSource = driver.page_source
pgSource


# In[21]:


# parsing 및 태그 값 접근
htmlObj = bs4.BeautifulSoup(pgSource, "html.parser")
TotalPage=htmlObj.find(name ="ul", attrs = {"class":"search_goods_list_box float01"} )
TotalPage


# In[22]:


NameList = []
PriceList = []


# In[23]:


NameInfo = TotalPage.findAll(name= "div", attrs={"class":"align_left line_h140"})
PriceInfo = TotalPage.findAll(name= "strong", attrs={"class":"color_2a"})


# In[24]:


for i in range(0,len(NameInfo),+2):
    eachName = NameInfo[i].text
    Name = eachName.replace("\n", "")
    NameList.append(Name) 
    
for j in range(0,len(PriceInfo)):
    Price = PriceInfo[0].text
    PriceList.append(Price)


# In[25]:


result = pd.DataFrame(zip(NameList,PriceList))


# In[26]:


columnTitle = ["이름", "가격"]


# In[27]:


result.columns = columnTitle


# In[28]:


result


# In[29]:


# CSV 파일로 저장
result.to_csv("./midterm.csv", encoding="ms949", index=False)


# In[30]:


# SMTP 프로토콜 로드
import smtplib

# 이메일을 간단하게 보낼 수 있는 라이브러리 로드
from email.message import EmailMessage


# In[31]:


# GMAIL 메일 설정
smtp_gmail = smtplib.SMTP('smtp.gmail.com', 587)

# 서버 연결 설정 및 연결 암호화
smtp_gmail.ehlo()
smtp_gmail.starttls()

# 로그인
userid = "gsj9171"
userpw = "zsjvjcyonylxegzu"


# In[32]:


# 데이터 저장
import pickle
with open('pw.pickle', 'rb') as handle:
    pwpickle = pickle.load(handle)
import getpass
smtp_gmail.login(userid, userpw)


# In[33]:


msg = EmailMessage()

# 제목, 내용, 보내는 사람, 받는 사람 입력
msg['Subject'] = "중간고사_고수진"
msg.set_content("중간고사 제출")
msg['From'] = 'gsj9171@gmail.com'
msg['To'] = 'gsj1250@naver.com'


# In[34]:


# 메일 전송
file = 'midterm.csv'
fp = open(file,'rb')
file_data=fp.read()
msg.add_attachment(file_data, maintype='text', subtype='plain', filename = file)
smtp_gmail.send_message(msg)
smtp_gmail.close()


# In[ ]:




