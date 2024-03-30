import requests
from bs4 import BeautifulSoup

#The code imports the necessary libraries for web scraping, namely requests for making HTTP requests and BeautifulSoup for parsing HTML.

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
#print("\n***Page***")
#print(page.text)
#print("***END***")

soup = BeautifulSoup(page.content, "html.parser")
#print ("\n***Soup***")
#print(soup)
#print("***END***")

results = soup.find(id="ResultsContainer")
#print ("\n***results***")
#print(results.prettify())
#print("***END***")

print ("\n***Job Element***")
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element)
    print(company_element)
    print(location_element)
    print()
    print(title_element.text)
    print(company_element.text)
    print(location_element.text)
    print()
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
print("***END***")

print ("\n***Python Job Element***")
python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
print("Number of elements: ", len(python_jobs))
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
print("***END***")
