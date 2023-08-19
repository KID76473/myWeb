import os
import json
from linkedin_scraper import JobSearch, actions, Job
from selenium import webdriver


# proxy_ip = "138.197.203.84"
# proxy_port = "7497"
#
# proxy = f"http://{proxy_ip}:{proxy_port}"
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f'--proxy-server={proxy}')  # change IP address
# chrome_options.add_experimental_option("detach", True)  # does not close webpage automatically
#
# driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome()

# email = "kid76473@gmail.com"
email = "13161133872@163.com"
password = "Hjjhjjhjj007"

# new_cookie = {
#     "name": email,
#     "value": password,
#     "domain": ".www.linkedin.cn",  # Replace with the appropriate domain
#     "path": "/",  # Replace with the appropriate path
# }
# actions._login_with_cookie(driver, new_cookie)

actions.login(driver, email, password, timeout=5)  # if email and password isn't given, it'll prompt in terminal
# input("Press Enter")
job_search = JobSearch(driver=driver, close_on_complete=True, scrape=True)
# job_search contains jobs from your logged in front page:
# - job_search.recommended_jobs
# - job_search.still_hiring
# - job_search.more_jobs

# Machine Learning Engineer
# Backend Engineer
# job_title = "Machine Learning Engineer"
job_title = input("Please input the job you want to search: ")
job_listings = job_search.search(job_title)  # returns the list of `Job` from the first
temp = {}
for j in job_listings:
    temp[j.job_title] = {
                         "title": j.job_title,
                         "company": j.company,
                         "location": j.location,
                         "benefits": j.benefits,
                         "description": j.job_description,
                         "url": j.linkedin_url
                        }

# Convert list to JSON
json_list = json.dumps(temp, indent=4)
print(json_list)

print("Start to write.")
desired_directory = "./data/"
file_name = job_title.replace(" ", "") + ".json"
file_path = desired_directory + file_name
print("file_name is ", file_name)
with open(file_path, 'w', newline="", encoding='utf-8') as file:
    file.write(json_list)
    # json.dump(json_list, file, indent=4)  # This way is not preferred because it squeezes all data into one line.
print("Finished.")
