import glob
import json
import os
import requests


files = [file for file in glob.glob('*.pdf')] + [file for file in glob.glob('*.doc')] + [file for file in glob.glob('*.docx')]

if not files:
    exit('No files found - make sure your files are in the \'src\' directory.')

for index, pdf in enumerate(files):
    print(f'{str(index + 1)} - {pdf}')

while True:
    try:
        option = int(input('Select file number or 0 to exit: ')) - 1

        if option == -1:
            exit()
        elif option in range(0, len(files)):
            resume_file = files[option]
            break
        else:
            print(f'Enter a valid number between 1 and {len(files)}')
    except ValueError:
        print(f'Enter a valid number between 1 and {len(files)}')

url = 'https://jobs.lever.co/parseResume'
resume, resume_file_path = open(resume_file, 'rb'), os.path.splitext(resume_file)[0] + '.txt'

response = requests.post(url, files={'resume': resume}, headers={'referer': 'https://jobs.lever.co/', 'origin': 'https://jobs.lever.co/'}, cookies={'lever-referer': 'https://jobs.lever.co/'})
parsed_resume = json.dumps(response.json(), indent=4)

save_response = open(resume_file_path, 'w')
save_response.write(parsed_resume)

print(f'Output saved as: {resume_file_path}')
