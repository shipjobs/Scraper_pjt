from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import csv
import time

jobs_db = []
  
  
def scraprt_wanted(keyworld):
  # playwright 을 사용하여 브라우저를 실행하고, 페이지를 열어서 스크린샷을 찍는 코드
  p = sync_playwright().start()
  browser = p.chromium.launch(headless=False) #True로 설정하면 브라우저가 실행되지 않음/차단됨
  page = browser.new_page()

  page.goto("https://www.wanted.co.kr/jobsfeed")
  #https://www.wanted.co.kr/search?query=flutter   #플러터 검색 결과 페이지

  time.sleep(1) # 5초간 대기

  #Aside_searchButton__rajGo Aside_isNotMobileDevice__hTNEe
  page.click("button.Aside_searchButton__rajGo")  # 선택
  time.sleep(1) # 5초간 대기
  # page.locator("button.Aside_searchButton__rajGo").click() # 유사 가능: 버튼 클릭

  page.get_by_placeholder("검색어를 입력해 주세요.").fill(f"{keyworld}") # 검색창에 "flutter" 입력
  time.sleep(1) # 5초간 대기

  page.keyboard.down("Enter") # 엔터키 입력
  time.sleep(1) # 5초간 대기

  page.click("a#search_tab_position")
  time.sleep(1) # 5초간 대기

  #브라우저에서의 결과 데이터 읽어오도록 하기
  for i in range(5):
      page.keyboard.down("End") # 엔터키 입력
      time.sleep(1) # 5초간 대기

  content = page.content()
  # print(content)

  page.screenshot(path="../../output/screenshot/screenshot.png")
  p.stop() # 브라우저 종료 , 메모리 해제

  soup = BeautifulSoup(content, "html.parser")
  jobs = soup.find_all("div", class_="JobCard_container__REty8")

  for job in jobs:
    # link = job.find("a")["href"]
    link = f"https://www.wanted.co.kr{job.find('a')['href']}"
    title = job.find("strong", class_="JobCard_title__HBpZf").text
    company_name = job.find("span", class_="JobCard_companyName__N1YrF").text
    # location = job.find("span", class_="JobCard_location__2gjg3").text
    reward = job.find("span", class_="JobCard_reward__cNlG5").text
    
    job = {
      "keword": keyworld,
      "link": link,
      "title": title,
      "company_name": company_name,
      "reward": reward
    }
    jobs_db.append(job)
    
  return jobs_db


if __name__ == "__main__":

  keywords = [
    "React",
    # "nextjs",
    # "django",
  ]

  for keyword in keywords:
    scraprt_wanted(keyword)
    time.sleep(1)

  # 데이터를 파일로 저장하기 위해 
  file = open("output/data/jobs.csv", "w", newline="", encoding="UTF-8")
  writer = csv.writer(file)
  writer.writerow(
    [
      "Keyword",  # "keword
      "link", 
      "title", 
      "company_name", 
      "reward"
      ]
    ) # 헤더 작성

  # jobs_db.values()
  for job in jobs_db:
    writer.writerow(list(job.values()))

  jobs_db.clear()
  file.close()