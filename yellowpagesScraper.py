# in terminal do: "sudo apt-get install python3-bs4"


import requests
from bs4 import BeautifulSoup

url = "https://www.yellowpages.com/search?search_terms=Coffee+Shops&geo_location_terms=davis%2Cca"
r = requests.get(url)

soup = BeautifulSoup(r.content)


links = soup.find_all("a")

for link in links:
	# if "http" in link.get("href"):
		#print("a href='%s'>%s</a>" %(link.get("href"), link.text))
#The g_data part looks for a specific div and class within our link, in this case we are looking for the coffee info
		g_data = soup.find_all("div", {"class": "info"})

data =[]

for item in g_data:
	# business_name = item.contents[0].find_all("a", {"class": "business-name"})[0].text
	print(item.contents[0].find_all("a", {"class": "business-name"})[0].text)
	
	# address = item.contents[1].find_all("p", {"class": "adr"})[0].text
	print(item.contents[1].find_all("p", {"class": "adr"})[0].text)
	
	try:
		# str_adr =item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text
		print(item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text)
	except:
		
		pass	
	try:
		print(item.contents[1].find_all("span", {"itemprop": "addressLocality"})[0].text.replace(',',''))	
	except:
		pass
	try:
		print(item.contents[1].find_all("span", {"itemprop": "addressRegion"})[0].text)	
	except:
		pass
	try:
		# postalCode = item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text
		print(item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text)	
	except:
		
		pass
	try:
		print(item.contents[1].find_all("div", {"class": "phones phone primary"})[0].text)
	except:
		pass

	# business = [business_name,address,str_adr,postalCode]
	# business_list.append(business_name,address,str_adr,postalCode)
	data.append((business_name,address,str_adr,postalCode))

import csv
with open ('index.csv','a') as csv_file:
	writer=csv.writer(csv_file)
	for name, price in data:
	writer.writerow([business_name,address,str_adr,postalCode])
	
		 

	# 	 data = {'business_name' : name,'address': adr,'str_adr': str_adr}
	# 	 def write_csv(data):
 # with open('yp.csv', 'a') as f:
 #  writer = csv.writer(f)
 #  writer.writerow( (data['name'],
 #        data['address'],
 #        data['str_adr'],
 #         ))
 #  write_csv(data)

	#the a, p, li are the type of elements


