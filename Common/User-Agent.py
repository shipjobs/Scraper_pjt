import requests


#url structure: https://remoteok.com/remote-golang-jobs

# keyworlds = [
#   "python",
#   "golang",
#   "flutter", 
# ]

#headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ 을 기입 하여 브라우저를 흉내
r = requests.get("https://remoteok.com/remote-golang-jobs" , 
                 headers={'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36}"})

print(r.status_code)  # 200 결과 확인
