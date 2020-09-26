import json
import requests

url = 'https://jobs.lever.co/parseResume'
resume = open('./sample.pdf', 'rb')

response = requests.post(url, files={ 'resume': resume })
parsed_resume = json.dumps(response.json(), indent=4)

save_response = open('output.txt', 'w')
save_response.write(parsed_resume)
