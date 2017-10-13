import csv
import urllib.request
from bs4 import BeautifulSoup
from google import search

count = 0

buyerName = "" #0
buyerCountry = "" #1
sellerName = "" #2
sellerImage = "" #3
sellerCountry = "" #4
sellerField = "" #5
sellerDesc = " " #6
valuation = "" #7 
moreInfo = " " #8
date = "" #9

fieldnames = ['Buyer Name', 'Buyer Country', 'Seller Name', 'Seller Image', 'Seller Country', 'Seller State',
		'Seller Field', 'Seller Desc', 'Valuation', 'More Info', 'Date']

outputCsv = open('C:\\PATH\\TO\\OUTPUT.csv', mode='w', encoding='IBM437')
with open('C:\\PATH\\TO\\INPUT.csv', mode='r', encoding='IBM437') as csvfile:
	acquiReader = csv.reader(csvfile)
	opener = urllib.request.build_opener()
	acquiWriter = csv.DictWriter(outputCsv, delimiter=',', lineterminator='\n', fieldnames=fieldnames)
	
	for row in acquiReader:
		buyerName = row[0]
		buyerCountry = row[1]
		sellerName = row[2]
		sellerImage = row[3]
		sellerCountry = row[4]
		sellerField = row[5]
		sellerDesc = row[6]
		valuation = row[7]
		moreInfo = row[8]
		date = row[9]
		title = " "
		titles = [" ", " ", " ", " ", " "]
		urls = [" ", " ", " ", " ", " "]
		descriptions = [" ", " ", " ", " ", " "]
		index = 0
		print(count)
		#Choose starting location (Cell row - 1)
		if(count > 3):
			print("Seller Name: " + sellerName)
			print("Search Text: " + (sellerName + " " + buyerName + " acquisition"))
			for url in search((sellerName + " " + buyerName + " acquisition"), stop=3):
				if(index < 4):
					try:
						external_sites_html = opener.open(url).read()
						urls[index] = url
						soup = BeautifulSoup(external_sites_html, "html.parser")
						print(index, ": ")
						if(soup.title):
							title = soup.title.string
						if(title):
							titles[index] = title
						print("Title: " + title)
						print("URL: " + url)
						description = soup.find('meta', attrs={'name':'og:description'}) or soup.find('meta', attrs={'property':'description'}) or soup.find('meta', attrs={'name':'description'})
						if description:
							descriptions[index] = description.get('content')
							print("Description: ", descriptions[index])
						print(" ")
					except urllib.request.HTTPError:
						print("Error")
					index += 1
			choice = input("Enter your choice: ")
			choice = int(choice)
			if(choice == 4):
				acquiWriter.writerow({'Buyer Name': buyerName, 'Buyer Country': buyerCountry, 'Seller Name': sellerName, 'Seller Image': sellerImage, 
					'Seller Country': sellerCountry, 'Seller Field': sellerField, 'Seller Desc': sellerDesc, 'Valuation': valuation, 'More Info': moreInfo, 
					'Date': date})
			else:	
				acquiWriter.writerow({'Buyer Name': buyerName, 'Buyer Country': buyerCountry, 'Seller Name': sellerName, 'Seller Image': sellerImage, 
					'Seller Country': sellerCountry, 'Seller Field': sellerField, 'Seller Desc': sellerDesc, 'Valuation': valuation, 'More Info': urls[choice], 
					'Date': date})
		count += 1
outputCsv.close()

