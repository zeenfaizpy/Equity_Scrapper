"""
Author: Mohammad Faizal Bin Zeenath Ali
Title: UnOfficial Scaping of Intra day price of Stocks

"""
import requests
from BeautifulSoup import BeautifulSoup as bs
from lxml.html.soupparser import fromstring
import re

symbol = raw_input('Enter Company Symbol ----> ')
# p = re.compile('[,;\s]+')
url = "http://nseindia.com/charts/webtame/tame_intraday_getQuote_closing_redgreen.jsp?CDSymbol=%s&Segment=CM&Series=EQ&CDExpiryMonth=&FOExpiryMonth=&IRFExpiryMonth=&CDDate1=&CDDate2=&PeriodType=2&Periodicity=1&Template=tame_intraday_getQuote_closing_redgreen.jsp" % (symbol)
r = requests.get(url)
result = fromstring(r.text)
data = result.find('.//data')
d = data.text.replace(",","|")
d = d.replace("\n",",").replace("\r","")

# """ Code to picks LTP"""
# sample = d.split(",")
# sample = sample[-1].split("|")
# print "Time----> %s" % (sample[0])
# print "LTP-----> %s" % (sample[-1])


"""Code to get all intra-day prices"""
for s in d.split(","):
	ss = s.split("|")
	print ss
