import requests
from bs4 import BeautifulSoup # This library parses the string get as a request and interprets it

url = "https://stackoverflow.com/questions"
response = requests.get(url)
response_text = response.text

soup = BeautifulSoup(response_text, "html.parser")
questions = soup.select(".s-post-summary") # Selecting components wih this class

for question in questions:
    question_title = question.select_one(".s-link").get_text()
    question_user = question.select_one(".s-user-card--link").get_text()
    question_id = question["data-post-id"] # With this we access to a value of an attribute
    
    print(f"Question {question_id}: {question_title} by {question_user.strip()}")