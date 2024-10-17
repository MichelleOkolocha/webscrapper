from bs4 import BeautifulSoup
import requests
import time
import os


def find_jobs():
    html_text = requests.get("https://weworkremotely.com/categories/remote-full-stack-programming-jobs").text #URL of the website to be scraped
    soup = BeautifulSoup(html_text, "html.parser") #Using Beautiful soup to parse the html
    jobs = soup.find_all("li", class_="feature") #Getting the list of all the job posts on this URL
     

    with open(f"C:/Users/MIO/Desktop/Codes/Job_Posts.txt", "a", encoding="utf-8") as f:
        
        f.write(f"\n")
        f.write(f"\n")
        f.write(f"\n")
        f.write(f"\n")
        text = "NEW BATCH"
        width = 50
        centered_text = text.center(width, "-")  # Use '-' as the padding character
        f.write(f"{centered_text}")
        f.write(f"\n")
        f.write(f"\n")
        f.write(f"\n")
                  
        

        for job in jobs:
            #Gets the job title, company name, job duration, posted date, job link and stores it in a variable
            job_posted_date = job.find("span", class_="listing-date__date").text.replace(" ","")
            job_title = job.find("span", class_ = "title").text.replace(" ","")

            company_spans = job.find_all('span', class_='company')#there were 2 span tags with the class "company" so I put both of them in a list and stored in a variable
            company_name = company_spans[0].text.replace(" ","")#this is calling the first of the span tags which holds the company name
            job_duration = company_spans[1].text.replace(" ","")#this is calling the second span tag job duration
            
            a_tags = job.find_all('a')#There a about 3 "a" tags which href values. So I did the same thing I did to the span tags.
            link = a_tags[1]['href']#this is calling the 'a' tag since it is only this one that I want.

            f.write(f"Job Title: {job_title}\n")
            f.write(f"Company Name: {company_name}\n")
            f.write(f"Date Posted: {job_posted_date}\n")
            f.write(f"Job Duration: {job_duration}\n")
            f.write(f"Link: https://weworkremotely.com{link}\n")
            f.write("\n" + "="*40 + "\n")  # Divider for each job entry
        print(f"File Saved: Job Posts")





if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10080
        print(f"Will run again after one week.....")
        time.sleep(time_wait * 60)


