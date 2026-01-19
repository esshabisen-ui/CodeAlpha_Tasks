import requests 
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
import random

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

job_data = []

def assign_salary(title):
    title = title.lower()
    if "data" in title:
        return "6-10 LPA"
    elif "engineer" in title:
        return "8-12 LPA"
    elif "developer" in title or "python" in title:
        return "5-9 LPA"
    else:
        return "4-6 LPA"

for job in jobs:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    
    salary = assign_salary(title)
    
    posted_days_ago = random.randint(1, 30)
    posted_date = (datetime.today() - timedelta(days=posted_days_ago)).date()
    
    job_data.append({
        "Job_Title": title,
        "Company": company,
        "Location": location,
        "Salary": salary,
        "Posted Date": posted_date
    })
    
df = pd.DataFrame(job_data)
df.to_csv("job_listings.csv", index=False)

print("Job listings data scraped successfully!")