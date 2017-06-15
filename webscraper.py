import requests
from bs4 import BeautifulSoup
import re
import sys

SHOPPING_URL = "http://www.shopping.com/products"

def getNumberOfResults(keyword):

    params = {
               "KW" : keyword
             }

    response = requests.get(SHOPPING_URL,params=params)

    soup = BeautifulSoup(response.text,'lxml')

    tag = soup.find('span',class_="numTotalResults")

    text = tag.getText().strip('\n')

    totalResults = re.search('of(.\d*)',text)
    totalPages = re.search("(.\d *)of",text)

    

    try:
        
        return int(totalResults.group(1)), int(totalPages.group(1))
    
    except (ValueError,TypeError,AttributeError):
        print("Oops, Something Went Wrong!")


def getResultsFromPage(keyword,page):

    params = {
               "KW" : keyword,
             }

    
    URL = SHOPPING_URL + '~PG-' + page
    
    response = requests.get(URL,params=params)

    soup = BeautifulSoup(response.text,'lxml')

    tags = soup.findAll('div',class_='gridItemBtm')

    products = []

    for tag in tags:

        try:
            productName = tag.findChild('a',class_="productName").findChild('span')['title']

            productPrice = tag.findChild('span',class_="productPrice").findChild('a').getText().strip('\n')


            products.append({
                             "productName":productName,
                             "productPrice":productPrice
                           })
        except AttributeError:
            continue


    return products


if __name__ == "__main__":

    argv = sys.argv[1:]

    if len(argv) == 1:

        numResults, numPages = getNumberOfResults(argv[0])

        if numResults:

            print("Total number of results for '{}' = {} in {} pages".\
                   format(argv[0],numResults,numPages))

    elif len(argv) == 2:

        numPages = getNumberOfResults(argv[0])[1]

        if numPages < int(argv[1]):
            print("Results for '{}' are only of {} pages, please enter a value less than {}".format(argv[0],numPages,numPages))

        else:
            products = getResultsFromPage(argv[0],argv[1])

            if not products:

                print("There are no products on the page {}".format(argv[1]))

            
            print("Found {} products for {} in page {}".format(len(products),argv[0],argv[1]))
            
            for product in products:

                print("Name: {} , Price: {}".format(product["productName"], product["productPrice"]))

    else:

        print('''Please follow either of the two options:
                 - python3 webscraper.py <keyword>
                 - python3 webscraper.py <keyword> <page_no>
              ''')









