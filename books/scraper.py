from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from .models import Book

def scrape_books(user):
    options = Options()
    options.add_argument('--headless')  
    driver = webdriver.Chrome(options=options)

    
    user_pages = {
        'name_of_user_1': [1, 2],
        'name_of_user_2': [3, 4],
        'name_of_user_3': [5, 6],
    }

    if user.is_superuser:
        pages = list(range(1, 51))  
    else:
        pages = user_pages.get(user.username, [])

    for page in pages:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        driver.get(url)
        time.sleep(1)

        books = driver.find_elements(By.CLASS_NAME, 'product_pod')

        for book in books:
            title_element = book.find_element(By.TAG_NAME, 'h3').find_element(By.TAG_NAME, 'a')
            title = title_element.get_attribute('title')
            price = book.find_element(By.CLASS_NAME, 'price_color').text
            stock = book.find_element(By.CLASS_NAME, 'instock').text.strip()

            
            book_link = title_element.get_attribute('href')
            driver.get(book_link)
            time.sleep(1)

            try:
                description_element = driver.find_element(By.ID, 'product_description')
                description = description_element.find_element(By.XPATH, 'following-sibling::p').text
            except:
                description = 'No description available'

            upc = driver.find_element(By.XPATH, '//th[text()="UPC"]/following-sibling::td').text
            num_reviews = driver.find_element(By.XPATH, '//th[text()="Number of reviews"]/following-sibling::td').text

            
            Book.objects.create(
                title=title,
                price=price,
                stock=stock,
                description=description,
                upc=upc,
                num_reviews=int(num_reviews),
                owner=user
            )

            driver.back()
            time.sleep(1)

    driver.quit()
