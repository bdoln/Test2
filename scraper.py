############################################################################### 
#STARTHERE:Tutorial3:Moreadvancedscraping.Showshowtofollow'next' 
#linksfrompagetopage:usefunctions,soyoucancallthesamecode 
#repeatedly.SCROLLTOTHEBOTTOMTOSEETHESTARTOFTHESCRAPER. 
###############################################################################

import scraperwiki 
import urlparse 
import lxml.html



#scrape_tablefunction:getspassedanindividualpagetoscrape
def scrape_table(root):
    rows = root.cssselect("table.data tr") # selects all <tr blocks within <table class="data"
    for row in rows:
        # Set up our data record - we'll need it later
        record = {}
        table_cells = row.cssselect("td") 
        if table_cells:
            record['Artist'] = table_cells[0].text 
            record['Album'] = table_cells[1].text 
            record['Released'] = table_cells[2].text 
            record['Sales m'] = table_cells[4].text 
            # Print out the data we've gathered 
            print record, '------------'
            # Finally, save the record to the datastore - 'Artist' is our unique key
            scraperwiki.sqlite.save(["Artist"], record)
          
#scrape_and_look_for_next_linkfunction:callsthescrape_table
#function,thenhuntsfora'next'link:ifoneisfound,callsitselfagain
def scrape_and_look_for_next_link(url):
  html = scraperwiki.scrape(url)
  print html
  root = lxml.html.fromstring(html)
  scrape_table(root)
  next_link = root.cssselect("a.next")
  print next_link
  if next_link:
    next_url = urlparse.urljoin(base_url, next_link[0].attrib.get('href'))
    print next_url
    scrape_and_look_for_next_link(next_url)
    
# ------------------------------------------------------------
# START HERE: define your starting URL - then
# call a function to scrape the first page in the series.
# -------------------------------------------------------------
base_url = 'https://paulbradshaw.github.io/'
starting_url = urlparse.urljoin(base_url, 'scraping-for-everyone/webpages/example_table_1.html')
scrape_and_look_for_next_link(starting_url)
            
