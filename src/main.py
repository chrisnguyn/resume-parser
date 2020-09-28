import glob
import json
import os
import requests


print('Scanning for resume(s)...')

files = [file for file in glob.glob('*.pdf')]

if len(files) == 0:
    print('No files found - please move files inside the src/ directory.')
    exit()

print('Resume(s) found...')

for index, pdf in enumerate(files):
    print(str(index + 1) + " - " + pdf)

if len(files) > 1:
    while True:
        try:
            option = int(input('Select file number: ')) - 1

            if option in range(0, len(files)):
                resume_file = files[option]
                break
            else:
                print('Please enter a valid number between 1 and ' + str(len(files)))
        except ValueError:
            print("Please enter a valid number between 1 and " + str(len(files)))    
else:
    resume_file = files[0]

url = 'https://jobs.lever.co/parseResume'
resume = open(resume_file, 'rb')
resume_file_path = os.path.splitext(resume_file)[0] + '.txt'

response = requests.post(url, files={'resume': resume})
parsed_resume = json.dumps(response.json(), indent=4)

save_response = open(resume_file_path, 'w')
save_response.write(parsed_resume)

print('Output saved as:', resume_file_path)