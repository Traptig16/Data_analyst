import pandas as pd
import requests
from bs4 import BeautifulSoup
URL=["https://www.flipkart.com/search?q=redmi+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_sc_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_sc_na_ps&as-pos=1&as-type=RECENT&suggestionId=redmi+mobiles%7CMobiles&requestId=da8d16f5-9ffa-47b1-85cb-b73d8b967517&as-searchtext=redmi+phlones&page=",
     "https://www.flipkart.com/search?q=vivo+mobile&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_4_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_3_4_na_na_ps&as-pos=3&as-type=RECENT&suggestionId=vivo+mobile&requestId=f88ec761-73d0-44ee-8625-c23b19dfa08f&as-searchtext=vivo&page=",
     "https://www.flipkart.com/search?q=one+plus+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=one+plus+mobile%7CMobiles&requestId=e4f93b5c-1fa6-423e-bcc3-93dd7a59fafb&as-searchtext=one+mobiles&page=",
     "https://www.flipkart.com/search?q=apple+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=apple+mobiles%7CMobiles&requestId=ba97bbd3-e68b-43e6-ad24-669dbe55e5b0&as-searchtext=appl&page="]
Product_name = []
Prices = []
Description = []
Reviews = []

for url in URL:
    for i in range(2,30):
        r = requests.get(url+str(i))
        soup = BeautifulSoup(r.text, "lxml")
        box=soup.find("div",class_="_1YokD2 _3Mn1Gg")
        name = box.find_all("div", class_="_4rR01T")
        for i in name:
            name = i.text
            Product_name.append(name)

        prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
        for i in prices:
            name = i.text
            Prices.append(name)
        desc=box.find_all("ul", class_="_1xgFaf")
        for i in desc:
            name=i.text
            Description.append(name)
        reviews=box.find_all("div", class_="_3LWZlK")
        for i in reviews:
            name=i.text
            Reviews.append(name)
data = zip(Product_name, Prices, Description, Reviews)
df = pd.DataFrame(columns=["Product Name", "Prices", "Description", "Reviews"])

for row in data:
    if len(row) == 4:
        df = pd.concat([df, pd.DataFrame([row], columns=["Product Name", "Prices", "Description", "Reviews"])], ignore_index=True)

df.to_csv("D:/Internship/trapti_flipkart6.csv")