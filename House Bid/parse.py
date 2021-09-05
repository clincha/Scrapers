import xlsxwriter
from bs4 import BeautifulSoup

workbook = xlsxwriter.Workbook('output/data.xlsx')
worksheet = workbook.add_worksheet()
row = 0
for page in range(1, 5):
    soup = BeautifulSoup(open("data/page" + str(page) + ".html"), "html.parser")

    flats = []
    for flat in soup.find_all("article", class_="property-result"):
        address = ""
        prices = {}

        for addressElement in flat.find_all("h2", class_="property-result__address"):
            address += addressElement.text

        for priceElement in flat.find_all("p", class_="price"):
            saleDate = priceElement.text[str(priceElement.text).find("on") + 3:]
            salePrice = priceElement.text[:str(priceElement.text).find("on")]

            flats.append((address, saleDate, salePrice))

    for address, date, price in flats:
        col = 0
        worksheet.write(row, col + 0, address)
        worksheet.write(row, col + 1, date)
        worksheet.write(row, col + 2, price)
        row += 1

workbook.close()
