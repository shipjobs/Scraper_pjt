import csv

# Path: Common/file.py
def save_to_file(filename, jobs):
    
    file = open(filename, "w", newline="", encoding="UTF-8")
    writer = csv.writer(file)
    
    # writer.writerow(jobs.keys())
    writer.writerow(
    [
        "Keyword",  # "keword
        "link", 
        "title", 
        "company_name", 
        "reward"
        ]
    ) # 헤더 작성
    
    for job in jobs:
        writer.writerow(list(job.values()))
        print(job.values())
    file.close()
  

# file = open("output/data/jobs.csv", "w", newline="", encoding="UTF-8")
# writer = csv.writer(file)

# writer.writerow(
#   [
#     "Keyword",  # "keword
#     "link", 
#     "title", 
#     "company_name", 
#     "reward"
#     ]
#   ) # 헤더 작성

# # jobs_db.values()
# for job in jobs_db:
#   writer.writerow(list(job.values()))

# jobs_db.clear()

