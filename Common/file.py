import csv

# Path: Common/file.py
def save_to_file(filename, jobs):
    file = open(f"{file=}.csv", "w", newline="", encoding="UTF-8")
    writer = csv.writer("Keyword,link,title,company_name,reward,URL\n")
    
    for job in jobs:
        writer.writerow(list(job.values()))
    file.close()
  
