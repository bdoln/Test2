####################################
#STARTHERE:Tutorial2:Basicscrapingandsavingtothedatastore.
#FollowtheactionslistedinBLOCKCAPITALSbelow.
####################################

import scraperwiki
html = scraperwiki.scrape('http://inmo.ie/6022')

#---------------------------
#1.ParsetherawHTMLtogettheinterestingbits-thepartinside<tdtags.
#--UNCOMMENTTHE6LINESBELOW(i.e.deletethe#atthestartofthelines)
#--CLICKTHE'RUN'BUTTONBELOW
#Checkthe'Console'tabagain,andyou'llseehowwe'reextracting
#theHTMLthatwasinside<td</tdtags.
#Weuselxml,whichisaPythonlibraryespeciallyforparsinghtml.
#---------------------------

import lxml.html
root = lxml.html.fromstring(html) #turnourHTMLintoanlxmlobject
tds = root.cssselect('td') #getallthe<tdtags

#---------------------------
#2.SavethedataintheScraperWikidatastore.
#--UNCOMMENTTHETHREELINESBELOW
#--CLICKTHE'RUN'BUTTONBELOW
#Checkthe'Data'tab-hereyou'llseethedatasavedintheScraperWikistore.
#---------------------------

for td in tds:
  print td.text_content() # just the text inside the HTML tag
for td in tds:
  record = { "td" : td.text_content() } # column name and value
  scraperwiki.sqlite.save(["td"], record) # save the records one by one
  
#---------------------------
#GobacktotheTutorialspageandcontinuetoTutorial3tolearnabout
#morecomplexscrapingmethods.
#---------------------------
