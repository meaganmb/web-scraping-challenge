from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_page = {}

    url = 'https://redplanetscience.com/'
    browser.visit(url)
    # Iterate through all pages
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain title and paragraph information
    Latest_news_title = soup.find_all('div', class_='content_title')[0].text
    mars_page['news_title'] = Latest_news_title
    article_paragraph = soup.find_all('div', class_='article_teaser_body')[0].text
    mars_page['news_description'] = article_paragraph


    url = 'https://spaceimages-mars.com'
    browser.visit(url)
    # Iterate through page
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    featured_image_url = soup.find('img', class_='headerimage fade-in')['src']
    mars_page['featured_image'] = url + featured_image_url

    url = 'https://galaxyfacts-mars.com'
    browser.visit(url)
    # Iterate through page
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    tables = pd.read_html(url)
    mars_df = tables[0]
    html_table = mars_df.to_html()
    mars_page['mars_earth_table'] = html_table


    url = 'https://marshemispheres.com/'
    browser.visit(url)
    hemisphere_image_url = []

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find_all('div', class_='description')

    for article in articles:
        try:
            title = article.find('h3').text
            img_link = article.find('a')
            link = article.a['href']
            image = url + link
            new_url = image
            browser.visit(new_url)

            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')
            result = soup.find('img', class_='wide-image')
            new_link = result['src']
            
            img_url = f"https://marshemispheres.com/" + new_link

            if (title and new_link):
                hemisphere_dict = {
                    'title' : title,
                    'img_url' : img_url}
                hemisphere_image_url.append(hemisphere_dict)
        except:
            print('e')
    
    mars_page['mars_hemispheres'] = hemisphere_image_url



    # Quit the browser
    browser.quit()

    return mars_page




