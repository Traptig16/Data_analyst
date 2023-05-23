import pandas as pd 
import requests
from bs4 import BeautifulSoup

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

SURLS = [
    "https://www.amazon.in/s?k=redmi+in+mobile&crid=2ABU4NBQAOHZW&qid={qid}&sprefix=redmi+in+%2Caps%2C335&ref=sr_pg_",
    "https://www.amazon.in/s?k=vivo+phones&i=electronics&rh=n%3A1389401031&qid=1684135771&ref=sr_pg__",
    "https://www.amazon.in/s?k=oneplus+in+mobile&crid=2IC8ETTVC20V5&qid=1683954125&sprefix=oneplus+in+mobile%2Caps%2C297&ref=sr_pg_",
    "https://www.amazon.in/s?k=Apple+in+mobile&crid=2FBELCLPDJGK5&qid=1683954258&sprefix=apple+in+mobile%2Caps%2C296&ref=sr_pg_",
]

Product_name = []
Prices = []
Reviews = []

for url in SURLS:
    for page in range(1, 31):
        full_url = url.format(qid=1683878381 + (page - 1) * 48)
        r = requests.get(full_url, headers=HEADERS)
        soup = BeautifulSoup(r.text, "html.parser")
        box = soup.find("div", class_="s-main-slot s-result-list s-search-results sg-row")

        names = box.find_all("span", class_="a-size-medium a-color-base a-text-normal")
        for i in names:
            name = i.text.strip()
            Product_name.append(name)

        prices = box.find_all("span", class_="a-price-whole")
        for i in prices:
            name = i.text.strip()
            Prices.append(name)

        reviews = box.find_all("span", class_="a-icon-alt")
        for i in reviews:
            name = i.text.strip()
            Reviews.append(name)

data = zip(Product_name, Prices, Reviews)
df = pd.DataFrame(columns=["Product Name", "Prices", "Reviews"])

for row in data:
    df = pd.concat([df, pd.DataFrame([row], columns=["Product Name", "Prices", "Reviews"])], ignore_index=True)
df.to_csv("C:\Users\trapt\OneDrive\Desktop\python\web scraping/trapti_amazon6.csv" , index=0)