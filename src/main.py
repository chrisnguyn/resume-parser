import glob
import json
import os
import requests

print("Scanning for resume(s)...")

# get all PDF files in current directory
files = [file for file in glob.glob("*.pdf")]
if len(files) == 0:
    print("No PDF(s) found")
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
        except ValueError:  # catch non-number input
            print("Please enter a number between 1 and " + str(len(files)))

print("Parsing...")

# if only 1 file, then select automatically
if len(files) == 1:
    resume_file_path = files[0]
else:
    resume_file_path = files[option]  # grab user selected file

url = 'https://jobs.lever.co/parseResume'
resume = open(resume_file_path, 'rb')

response = requests.post(url, files={'resume': resume})
parsed_resume = json.dumps(response.json(), indent=4)

# remove.pdf extension from filename and add .txt
resume_file_path = os.path.splitext(resume_file_path)[0] + ".txt"

save_response = open(resume_file_path, 'w')
if save_response.write(parsed_resume):
    print("Resume parsed as: " + resume_file_path)
else:
    print("Error! Please try again")  # in case anything goes wrong
