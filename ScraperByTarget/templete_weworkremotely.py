# weworkremotely 사이트에서 Full Stack Programming 직군의 모든 페이지를 스크래핑하는 코드
# 작성자: 이인성
# 작성일: 2024.06.14

import requests
from bs4 import BeautifulSoup

all_jobs = []

#주소
#target_url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"
full_time_url = " https://weworkremotely.com/remote-full-time-jobs?page=1"

# 페이지를 스크래핑하는 함수
def scrape_page(target_url):

  print(f"Scrapping {target_url}...")
  
  response = requests.get(target_url)
  soup = BeautifulSoup(response.content, "html.parser")

  # jobs = soup.find("section", id="category-2")
  jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

  for job in jobs:
    title = job.find("span", class_="title").text
    results = job.find_all("span", class_="company") #span태그의 company 클래스를 가진 모든 요소를 찾아서 results에 저장
    
    # class가 "tooltip--flag-logo"인 div 태그를 찾음
    tooltip_div = job.find("div", class_="tooltip--flag-logo") # href 속성을 가진 a태그 앞에 있는 div태그를 찾음
    
    url = None
    # url = job.find("a")["href"] #a태그의 href 속성을 추출
    if tooltip_div is not None:
        next_sibling = tooltip_div.next_sibling # tooltip_div 의 다음 형제 요소를 찾음
        if next_sibling is not None:
            url = next_sibling.get("href")
            # print(url)
        else:
            print("다음 형제 요소가 없습니다.")
    else:
        print("Tooltip div를 찾을 수 없습니다.")
      
    if len(results) >= 3:
      company, postion, region = results[:3] 
    else:
      print("============== [No company, position, region] =============")

    job_data = {
        "title": title,
        "company": company.text,
        "postion": postion.text,
        "region": region.text,
        "url" : f"https://weworkremotely.com{url}"
    }
    all_jobs.append(job_data)
    

# 페이지 수를 가져오는 함수
def get_pages(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  page_cnt = len(soup.find("div", class_="pagination").find_all("span", class_ = "page")) #pagination 클래스를 가진 div태그의 모든 span태그를 찾아서 buttons 에 저장 (페이지 카운트)
  
  return page_cnt


# 본문 실행
total_pages = get_pages(full_time_url) # 페이지 수를 가져옴


for x in range(1, total_pages +1 ):     # 페이지 수만큼 반복
  url = f"https://weworkremotely.com/remote-full-time-jobs?page={x}"
  scrape_page(url) 

print(all_jobs)



