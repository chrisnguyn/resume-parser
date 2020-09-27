import json
import requests
import glob
import os

print("Scanning for resume(s)...")

files = [f for f in glob.glob("*.pdf")]
if len(files) == 0:
    print("No PDF found")
    quit()

print("Resume(s) found:")
for index, pdf in enumerate(files):
    print(str(index+1) + ". " + pdf)

if not len(files) == 1:  # if more than 1 resume exist
    while True:
        try:
            option = int(input("Select file number: ")) - 1
            if option in range(0, len(files)):
                break
            else:
                print("Please enter a number between 1 and " + str(len(files)))
        except ValueError:
            print("Please enter a number!")

print("Parsing...")
if len(files) == 1:
    f = files[0]
else:
    f = files[option]  # grab user selected

url = 'https://jobs.lever.co/parseResume'
resume = open(f, 'rb')

response = requests.post(url, files={'resume': resume})
parsed_resume = json.dumps(response.json(), indent=4)

f = os.path.splitext(f)[0] + ".txt"  # remove.pdf and add .txt

save_response = open(f, 'w')
if save_response.write(parsed_resume):
    print("Resume parsed as: " + f)
