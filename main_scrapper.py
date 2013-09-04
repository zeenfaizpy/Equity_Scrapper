"""
Author: Mohammad Faizal Bin Zeenath Ali
Title: UnOfficial Scaping of Main Stock Details.

"""
import requests
import re
import json

symbol = raw_input('Enter Company Symbol ----> ')

p = re.compile('/^\s+|\s+$/g')
payload = {"symbol" : symbol , "series" : "EQ"}
url = "http://nseindia.com/live_market/dynaContent/live_watch/get_quote//ajaxGetQuoteJSON.jsp"
r = requests.get(url,params = payload)
print r.headers['content-type']
data = r.json()


# print "-----------------------------------------------------"
# for k,v in data["data"][0].iteritems():
# 	print "%s ------>  %s" %(k,v)
# print "-----------------------------------------------------"



print "-----------------------------------------------------"
print "Company Name ---> %s" % (data["data"][0]["companyName"])
print "Symbol ---> %s" % (data["data"][0]["symbol"])
print "Last Price ----> %s" %(data["data"][0]["lastPrice"])
print "Change In Value ----> %s" %(data["data"][0]["change"])
print "Change In Percentage----> %s" %(data["data"][0]["pChange"])
print "Day High ----> %s" %(data["data"][0]["dayHigh"])
print "Day Low ----> %s" %(data["data"][0]["dayLow"])
print "52 Week High ----> %s - %s" %(data["data"][0]["high52"],data["data"][0]["cm_adj_high_dt"])
print "52 Week Low ----> %s - %s" %(data["data"][0]["low52"],data["data"][0]["cm_adj_low_dt"])
print "Average Price ----> %s" %(data["data"][0]["averagePrice"])
print "Open Price ----> %s" %(data["data"][0]["open"])
print "Close Price ----> %s" %(data["data"][0]["closePrice"])
print "Total Traded Volume ----> %s" %(data["data"][0]["totalTradedVolume"])
print "Total Traded Value ----> %s" %(data["data"][0]["totalTradedValue"])
print "Average Price ----> %s" %(data["data"][0]["averagePrice"])
print "ISIN CODE ----> %s" %(data["data"][0]["isinCode"])
print "Quantity Traded ----> %s" %(data["data"][0]["quantityTraded"])
print "----------------------------------------"



# print data["lastPrice"]
# print data["pChange"]
# print data["tradedValue"]
# print data["tradedVolume"]
# print data["marketCapitalization"]
# print data["vwap"]
# print data["beta"]
# print data["faceValue"]
# print data["bookValue"]
# print data["eps"]
# print data["payoutRatio"]
# print data["dividentCover"]
# print data["peRatio"]
# print data["exDate"]
# print data["corporateAction"]
# print data["quantityTraded"]
# print data["deliveryQuantity"]
# print data["deliveryToTradedQuantity"]
# print data["securityVar"]
# print data["varMargin"]
# print data["applicableMargin"]
# print data["extremeLossMargin"]