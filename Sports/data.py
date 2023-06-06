from datetime import datetime
from bs4 import BeautifulSoup
from Sports.settings import BASE_DIR
from DB.models import New,Blog,Refresh

links = {
    "All Headlines":"https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30",
    "Top Headlines":"https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&aggregateId=7f83e8ca-6701-5ea0-96ee-072636b67336",
    "MLB":"https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30&tags=fs/mlb",
    "NFL":"https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30&tags=fs/nfl",
    "College Football":"https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30&tags=fs/cfb",
    "USFL":"https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30&tags=fs/usfl",
    "NBA":"https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30&tags=fs/nba",
    "NHL":"https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30&tags=fs/nhl",
    "College Basketball":"https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30&tags=fs/cbk",
    "NASCAR":"https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30&tags=fs/truck-series,fs/cup-series,fs/xfinity-series",
    "UFC":"https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30&tags=fs/ufc",
    "Motor Sports":"https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30&tags=fs/indycar,fs/formula-1",
    "Golf":"https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30&tags=fs/korn-ferry-tour,fs/lpga-tour,fs/pga-tour",
    "Soccer":"https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30&tags=fs/soccer,soccer/epl/league/1,soccer/mls/league/5,soccer/ucl/league/7,soccer/europa/league/8,soccer/wc/league/12,soccer/euro/league/13,soccer/wwc/league/14,soccer/nwsl/league/20,soccer/cwc/league/26,soccer/gold_cup/league/32,soccer/unl/league/67",
    "Olympics":"https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30&tags=fs/winter,fs/summer",
    "Tennis":"https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30&tags=fs/atp,fs/wta",
    "Horseracing":"https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30&tags=fs/horseracing",
    "WNBA":"https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30&tags=fs/wnba",
    "Women College Basketball":"https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30&tags=fs/wcbk",
}

categories = [
        "UFC",
        "Golf",
        "USFL",
        "NBA",
        "NHL",
        "MLB",
        "NFL",
        "WNBA",
        "Soccer",
        "Tennis",
        "NASCAR",
        "Olympics",
        "Horseracing",
        "Motor Sports",
        "All Headlines",
        "Top Headlines",
        "College Football",
        "College Basketball",
        "Women College Basketball",
]

def clean(string):
    string = string.replace("	",'')
    string = string.replace("\n",'')
    string = string.replace(' ','-')
    string = string.replace('/','-')
    string = string.replace('?','')
    string = string.replace('|','')
    return string

def data(ourCategory):
    print("Data running")
    #------------------------<Temporary>----------------------

    url = links[ourCategory]
    file_name = ourCategory+".rss"
    with open(BASE_DIR/'Rss feed'/file_name,'r',encoding="UTF-8") as f:
        htmlContent = f.read()

    #-----------------------<Scraping>------------------------------
    # for live data extraction
    # res = requests.get(url)
    # htmlContent = res.content
    soup = BeautifulSoup(htmlContent,'xml')
    items = soup.find_all('item')

    #-------------------------<Fetching Data>--------------------------
    rank = 0
    for item in items:
        rank += 1 
        blog_url = clean((item.find('title')).get_text())
        title = blog_url.replace("-"," ")
        desc = (item.find('description')).get_text()
        pubDate = (item.find('pubDate')).get_text()
        medContent = (item.find('media:content'))['url']
        medThumbnail = (item.find('media:thumbnail'))['url']
        link = (item.find('link')).get_text()
        category = (item.find('category')).get_text()

        # print(rank,category,title)
    #---------------------------<Inseting New Data>-----------------
        try:
            obj = New.objects.filter(our_category=ourCategory,rank=rank)
            obj = obj[0]
        except:
            obj = New()

        obj.rank = rank
        obj.title = title
        obj.description = desc
        obj.publish_date = pubDate
        obj.category = category
        obj.our_category = ourCategory
        obj.media = medContent
        obj.thumbnail = medThumbnail
        obj.link = link
        obj.blog_url = blog_url

        obj.save()

        try:
            obj = Blog.objects.filter(title=title)
            obj = obj[0]
        except:
            obj = Blog()

        obj.rank = rank
        obj.title = title
        obj.description = desc
        obj.publish_date = pubDate
        obj.category = category
        obj.our_category = ourCategory
        obj.media = medContent
        obj.thumbnail = medThumbnail
        obj.link = link
        obj.blog_url = blog_url

        obj.save()

def ref_time(category):
    try:
        #--------------------Obtaining old time

        obj = Refresh.objects.get(name=category)
        # obj = obj[0]
        last_time = datetime.strptime(obj.time,"%Y-%m-%d, %H:%M")

        #--------------------Calculating difference

        current_time = datetime.now()
        diff = ((current_time-last_time).total_seconds())/60

        #--------------------Entering object for first time

    except:
        obj = Refresh(
            name = category,
            time = datetime.strftime(datetime.now(),"%Y-%m-%d, %H:%M")
        )
        obj.save()
        diff = 60

        #-----------------------Returning bool

    if diff>59:
        obj.time = datetime.strftime(datetime.now(),"%Y-%m-%d, %H:%M")
        obj.save()
        return True
    return False



