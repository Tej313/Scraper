import re
from collections import Counter
from bs4 import BeautifulSoup
import requests
import json

def extract_phrases(text):
    """
    Extracts phrases from text using a regular expression.
    
    Args:
        text (str): The text to extract phrases from.
        
    Returns:
        list: A list of lowercase phrases.
    """
    phrases = re.findall(r'\b\w+\s\w+\b', text)
    return [phrase.lower() for phrase in phrases]

# Fetch HTML content from the given URL
response = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?'
    'searchType=personalizedSearch&from=submit&'
    'searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation='
)

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all job postings
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

# List to store all skills mentioned in the job descriptions
all_skills = []

for job in jobs:
    skills = job.find('span', class_='srp-skills').text.strip()
    all_skills.extend(extract_phrases(skills))

# Count the frequency of each skill
skill_counter = Counter(all_skills)

# Extract the top 10 most common skills
top_skills = skill_counter.most_common(10)

# Print the top 10 phrases in job descriptions
print('Top 10 phrases in job descriptions:')
for skill, frequency in top_skills:
    print(f"{skill}: {frequency}")

# Save the top skills to a JSON file
top_skills_dict = {skill: frequency for skill, frequency in top_skills}

with open('top_skills.json', 'w') as json_file:
    json.dump(top_skills_dict, json_file, indent=4)

print('Top skills data has been saved to top_skills.json')
