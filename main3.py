from bs4 import BeautifulSoup
import requests
import time

print("Put Some Skills you are not interested in")
unfimiliar_skills = input(">")
print(f'Filtering Out{unfimiliar_skills}')
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span',class_='sim-posted').span.text
        if 'few' in published_date:
            skill = job.find('span',class_='srp-skills').text.replace(' ','')
            if unfimiliar_skills not in skill:
                company_name = job.find('h3',class_='joblist-comp-name').text
                more_info = job.header.h2.a['href']
                with open(f'posts/{index}.txt','w+') as f:
                    f.write(f"Company Name : {company_name.strip()}")
                    f.write(f"Skills Required : {skill.strip()}")
                    f.write(f"Published Date : {published_date.strip()}")
                    f.write(f"More Info : {more_info}")
                    f.write('-------------------------------------------')
                print(f'File Saved with Name : {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print('')
        print('-------------------------------')
        print(f'Waiting {time_wait} Minutes...')
        print('-------------------------------')
        print('')
        time.sleep(time_wait * 60)
