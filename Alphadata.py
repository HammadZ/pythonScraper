# in terminal do: "sudo apt-get install python3-bs4"
# This python scraper will iterate through multiple pages 
# This one prints in lines - better for excel, but suspicious that there may be a loss of data

import requests
from bs4 import BeautifulSoup


def StateIter():

	url = "https://www.yellowpages.com/search?search_terms=breweries&geo_location_terms="

	multiple_pages = url
	new_link =[]
	for i in range(51):
		states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
		new_link.append(multiple_pages + str(states[i]))
			# print(new_link[i])

	
	return new_link



arry = StateIter()
# for i in range(50):
# 	print(arry[i])


def PagesIter(arry):
	multiple_pages=[]
	
	for i in range(51):
		multiple_pages.append(str(arry[i]) + "&s=name" + '&page=')
		# print(multiple_pages[i])
		
	return multiple_pages

hooray = PagesIter(arry)

def StatesAndPages(hooray):
	newer_link =[]
	
	for i in range(51):
		for j in range(35):
			newer_link.append(hooray[i] + str(j+1))

	return newer_link



bubbles = StatesAndPages(hooray)

for i in range(2000):
	r = requests.get(bubbles[i])
		# soup = BeautifulSoup(r.content)
	soup = BeautifulSoup(r.content, "html.parser")
	links = soup.find_all("a")

	for link in links:
			# if "http" in link.get("href"):
			#print("a href='%s'>%s</a>" %(link.get("href"), link.text))
		#The g_data part looks for a specific div and class within our link, in this case we are looking for the coffee info
			g_data = soup.find_all("div", {"class": "info"})


	for item in g_data:
	
		First = item.contents[0].find_all("a", {"class": "business-name"})[0].text
		# print(item.contents[1].find_all("p", {"class": "adr"})[0].text)
		
		try:
			A = item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text.replace('¬† ','')
			# print(item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text,',')
			
		except:
			pass	
		try:
			#addressLocality is the city
			B=item.contents[1].find_all("span", {"itemprop": "addressLocality"})[0].text.replace(',','')
		except:
			pass
		try:
			C=item.contents[1].find_all("span", {"itemprop": "addressRegion"})[0].text	
		except:
			pass
		try:
			D =item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text
		except:	
			pass
		try:
			E=item.contents[1].find_all("div", {"class": "phones phone primary"})[0].text

		except:
			pass
		print(First,',',A,',',B,',',C,',',D,',',E,)
	
#Iterate through states
# states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
#           "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
#           "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
#           "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
#           "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

# url = "https://www.yellowpages.com/search?search_terms=breweries&geo_location_terms=California&s=name"
# multiple_pages = url + '&page='

# multiple_pages = url + '&page='+str(2)
# page_number = 35
