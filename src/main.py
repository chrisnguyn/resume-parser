"""
Lever is a company that produces recruiting software. Other companies use Lever to host their job postings.

When you apply to a job using that uses the Lever platform, there's a button to upload your resume.

Looking in the network tab when you upload your resume, we see it's sent to 'https://jobs.lever.co/parseResume'.

It's returned in our Network tab, and we see in 'Network > Response' we see it returns a JSON object with our parsed resume.

Clicking on 'parsedResume' and going to 'Network > Headers', we can scroll to the bottom and see 'Form Data - resume: (binary)'

So, all we need to do is make a POST request to that URL, with a form with key 'resume' = to our resume file.

We'll get it's response and capture it to a file.
"""

import json
import requests

url = 'https://jobs.lever.co/parseResume'
resume = open('./sample.pdf', 'rb')  # read mode, send as binary instead of text

response = requests.post(url, files={ 'resume': resume })  # we see in Network > Headers, it's looking for a key 'resume'
parsed_resume = json.dumps(response.json(), indent=4)  # get json from response, then pretty print with dumps()

save_response = open('output.txt', 'w')
save_response.write(parsed_resume)