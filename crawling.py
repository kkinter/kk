from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re
import sqlite3

def connect():
    conn=sqlite3.connect("k.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text,author text, year interger, isbn interger)")
    conn.commit()
    conn.close()

connect()

url ="https://book.naver.com/bestsell/bestseller_list.nhn"

driver =webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)

driver.get(url)
bs = BeautifulSoup(driver.page_source, 'html.parser')

page_urls = []
for i in range(0, 6):
    data = bs.find('dt', {'id':"book_title_"+str(i)})
    link = data.select('a')[0].get('href')
    page_urls.append(link)

for i , page_url in enumerate(page_urls):

    driver.get(page_url)
    bs = BeautifulSoup(driver.page_source, 'html.parser')

    title = bs.find('meta', {'property':'og:title'}).get('content')
    author = bs.find('dt', text='저자').find_next_siblings('dd')[0].text.strip()
    year = bs.find('dt', text='출판일').find_next_siblings('dd')[0].text.strip()
    a = bs.find('div',{'class':'txt_desc'}).find_next_siblings('div')[0].find_next_siblings('div')[0].text
    pattern = re.compile(r'[0-9]{5,15}')
    b = re.search(pattern, a)
    isbn = str(b.group())
    con = sqlite3.connect("k.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    con.commit()
    con.close()
    



