import csv
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

actions.login(driver, email, password, timeout=10)  # if email and password isn't given, it'll prompt in terminal
input("Press Enter")
job_search = JobSearch(driver=driver, close_on_complete=True, scrape=True)
# job_search contains jobs from your logged in front page:
# - job_search.recommended_jobs
# - job_search.still_hiring
# - job_search.more_jobs

# Machine Learning Engineer
# Backend Engineer
job_listings = job_search.search("Machine Learning Engineer")  # returns the list of `Job` from the first

print("Start to write.")
file = 'machineLearning.csv'
with open(file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for j in job_listings:
        writer.writerow([j.job_title, j.company])
print("Finished.")
