from bs4 import BeautifulSoup as soup

with open("data.xml","rt") as xmlFile:
    xml = soup(xmlFile, "html.parser")

    print xml.slide
    print xml.slide["type"]
    print xml.item

    print xml.find_all("customer")
