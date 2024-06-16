from requests import get 
# from random import randint

websites = (
  "google.com",
  "youtube.com",
  "https://facebook.com",
  "instagram.com",
  "twitter.com",
  "linkedin.com"
  # 공공데이터 포털
  # 지역 게시판
  # SNS
)

results = {}

for website in websites:
  # print('Website:', website)
  if not website.startswith('https://'):
    website = f'https://{website}'
    response = get(website)
    
    if response.status_code == 200:
      print(f'Website: {website} is OK and running')
      results[website] = 'OK'
    else:
      print(f'Website: {website} is FAILED')
      results[website] = 'FAILED'
      
print(results)

