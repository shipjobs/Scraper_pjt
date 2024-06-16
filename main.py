from requests import get 
from flask import Flask, render_template , request  

from ScraperByTarget.dynamic_site.templete_wanted import scraprt_wanted 
from Common.file import save_to_file

app = Flask("JobScrapper")

@app.route('/')
def home():
  # return "<h1>Hello, World!<h1><a href='/hello'>Hello</a>"
  return render_template("home.html", name="insung")


@app.route('/search')
def search():
    print(request.args)  #ImmutableMultiDict([('keyword', '123'), ('name', '123')])  
    keyword = request.args.get("keyword")
  
    read_job = scraprt_wanted(keyword)  #wanted 사이트에서 키워드에 해당하는 데이터를 가져온다.
    
    save_to_file("output/data/jobs.csv", read_job)

    return render_template("search.html" , keyword=keyword)


app.run("127.0.0.1", port=5000, debug=True)
