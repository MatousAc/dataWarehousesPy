import re
from urllib.request import urlopen
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
weatherData = client["weatherData"]

# Load website indicated by url
def load_url(url):
    page = urlopen(url)
    page_content = page.read().decode("utf-8")
    return page_content

def get_filenames_from_db():
    return list(weatherData.sauWeather.distinct('_id'))

def load_data_to_db(filename, json_weather_data):
    testData = weatherData.sauWeather.insert_one({
        '_id': filename,
        'data': json_weather_data
    })
    print(filename)

# Extract list of file names from website
html = load_url("http://tumnus.cs.southern.edu/jsonlog/")
files = re.findall(">ws.*json<", html, re.IGNORECASE)

# Clean file names from website
filenames = ' '.join(files).replace('>', '').replace('<', '').split()


# Get list of file names already in database
# and compare against filenames from website
# to get only file names not already in database

existing_filenames = get_filenames_from_db()
missing_files = list(set(filenames).difference(existing_filenames))


# Go over list of missing files and load json to database

for filename in missing_files:
    file_url = "http://tumnus.cs.southern.edu/jsonlog/" + filename
    json_weather_data = load_url(file_url)
    load_data_to_db(filename, json_weather_data)
