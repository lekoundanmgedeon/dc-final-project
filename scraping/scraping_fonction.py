import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import get

"""
The whole detailed of this code you'll find it in the scrapping notebook inside scrapping.
Notice this is the optimized function for streamlit that makes exactly same thing as did on notebook.
You can test it in website version and give link and pages number for scrapping

"""

def scrape_page(base_url, page_number):
    """Scrape only one page."""
    
    # add url and number of pages
    url = f"{base_url}?page={page_number}"

    res = get(url)
    soup = bs(res.content, "html.parser")

    containers = soup.select("div.card.ad__card")
    data = []

    for container in containers:
        try:
            # extract listing link
            a_tag = container.find("a", href=True)
            if not a_tag:
                continue

            product_url = "https://sn.coinafrique.com" + a_tag["href"]

            # open detail page
            detail_res = get(product_url)
            soup_detail = bs(detail_res.content, 'html.parser')

            # title
            title_tag = soup_detail.find("h1")
            title = title_tag.get_text(strip=True) if title_tag else None

            # price
            price_tag = container.select_one("p.ad__card-price a")
            if price_tag:
                price_raw = price_tag.get_text(strip=True)
                price = price_raw.replace("CFA", "").replace(" ", "")
            else:
                price = None

            # location
            loc_span = container.select_one("p.ad__card-location span")
            location = loc_span.get_text(strip=True) if loc_span else None

            # image
            img_tag = soup_detail.find("img", class_="ad__card-img")
            if not img_tag:
                img_tag = soup_detail.find("img")
            image_link = img_tag["src"] if img_tag else None

            data.append({
                "title": title,
                "price": price,
                "location": location,
                "image": image_link,
                "url": product_url
            })

        except Exception as e:
            print("Error:", e)
            continue

    return data



def scrape_pages(base_url, total_pages):
    """scrappe many pages on save it in dataframe."""
    
    df = pd.DataFrame()

    for page in range(1, total_pages + 1):
        print(f"Scraping page {page}...")
        page_data = scrape_page(base_url, page)

        if len(page_data) == 0:
            print("Probably empty page.")
            break

        df_page = pd.DataFrame(page_data)
        df = pd.concat([df, df_page], axis=0).reset_index(drop=True)

    print("Scraping completed!")
    return df

## I supposed to add database script here, but it's already done with notebook version
## I Strong recommend to go in this file and check it there.!
#### Thank you Mr Abdoul Wahab 
