from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    url = 'https://redplanetscience.com/'
    browser.visit(url)
    # Iterate through all pages
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain title and paragraph information
    Latest_news_title = soup.find_all('div', class_='content_title')[0].text
    article_paragraph = soup.find_all('div', class_='article_teaser_body')[0].text
    print(Latest_news_title)
    print(article_paragraph)


    url = 'https://spaceimages-mars.com'
    browser.visit(url)
    # Iterate through page
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    featured_image_url = soup.find('img', class_='headerimage fade-in')['src']


    url = 'https://galaxyfacts-mars.com'
    browser.visit(url)
    # Iterate through page
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    tables = pd.read_html(url)
    tables
    mars_df = tables[0]
    mars_df.head()
    mars_df.columns = ["Planet Facts", "Mars", "Earth"]
    mars_df
    html_table = mars_df.to_html()
    html_table
    html_table.replace('\n', '')
    mars_df.to_html('table.html', index = False)
    get_ipython().system('open table.html')


    url = 'https://marshemispheres.com/'
    browser.visit(url)
    hemisphere_image_url = []
    # Iterate through all pages

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain book information
    articles = soup.find_all('div', class_='description')

    for article in articles:
        try:
            title = article.find('h3').text
            img_link = article.find('a')
            link = article.a['href']
            image = url + link
            print('-----------')
            print(image)
            new_url = image
            browser.visit(new_url)

            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')
            result = soup.find('img', class_='wide-image')
            new_link = result['src']
            
            img_url = f"https://marshemispheres.com/" + new_link

            if (title and new_link):
                print(title)
                print(img_url)
                hemisphere_dict = {
                    'title' : title,
                    'img_url' : img_url}
                hemisphere_image_url.append(hemisphere_dict)
        except:
            print('e')



    # Quit the browser
    browser.quit()

    return listings




