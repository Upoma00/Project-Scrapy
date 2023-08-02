import requests
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
url = "https://www2.hm.com/en_us/women/new-arrivals/view-all/_jcr_content/main/productlisting.display.json?sort=stock&image-size=sm"
page = requests.get(url, headers=headers)
response = page.json()

HMData = []
for product_all in range(len(response["products"])):
    Productwisedata = {
        "Title": response["products"][product_all]["title"],
        "Price": response["products"][product_all]["price"],
        "Red Price": response["products"][product_all]["redPrice"],
        "Yellow Price": response["products"][product_all]["yellowPrice"],
        "Blue Price": response["products"][product_all]["bluePrice"],
        "Brand Name": response["products"][product_all]["brandName"],
        "Category": response["products"][product_all]["category"],
        "Swatches Total": response["products"][product_all]["swatchesTotal"],
        "Selling Attribute": response["products"][product_all]["sellingAttribute"],
        "Link": "https://www2.hm.com" + response["products"][product_all]["link"]
    }
    HMData.append(Productwisedata)

df = pd.DataFrame(HMData)
df.to_csv('HMData.csv', index=False)


