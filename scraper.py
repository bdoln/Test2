####################################
#STARTHERE:Tutorial2:Basicscrapingandsavingtothedatastore.
#FollowtheactionslistedinBLOCKCAPITALSbelow.
####################################

import scraperwiki
html = scraperwiki.scrape('http://inmo.ie/6022')
print "Click on the ...more link to see the whole page"
print html

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
for td in tds:
  print lxml.html.tostring(td) # the full HTML tag
  print td.text # just the text inside the HTML tag

#---------------------------
#2.SavethedataintheScraperWikidatastore.
#--UNCOMMENTTHETHREELINESBELOW
#--CLICKTHE'RUN'BUTTONBELOW
#Checkthe'Data'tab-hereyou'llseethedatasavedintheScraperWikistore.
#---------------------------

for td in tds:
  record = { "td" : td.text } # column name and value
  try:
    scraperwiki.sqlite.save(["td"], record) # save the records one by one
  except:
    record = { "td" : "NO ENTRY" } # column name and value
    scraperwiki.sqlite.save(["td"], record) # save the records one by one

#---------------------------
#GobacktotheTutorialspageandcontinuetoTutorial3tolearnabout
#morecomplexscrapingmethods.
#---------------------------
