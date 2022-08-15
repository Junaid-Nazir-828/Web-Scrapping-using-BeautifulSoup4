from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content,'lxml')
    course_cards = soup.find_all('div',class_= 'card')
    for i in course_cards:
        course_name = i.h5.text
        course_price = i.a.text.split()[-2] +" "+ i.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')
        
