from urllib2 import urlopen
from json import load
# country_code = 'ke'
country_code = raw_input("Please Enter iso2Code for Country: ").lower()

# Gets country profile from WorldBank in json format(which is actually a lis of dictionaries

request = 'http://api.worldbank.org/countries/%s?format=json'%(country_code)
response = urlopen(request)
json_dict1 = load(response)

# Prints out country profile to console

print 'Country Name: ' + str(json_dict1[1][0]['name'])
print 'Country\'s Capital: ' + str(json_dict1[1][0]['capitalCity'])
print 'Country\'s Region: ' + str(json_dict1[1][0]['region']['value'])
print 'Country\'s Income Level' +str(json_dict1[1][0]['incomeLevel']['value'])
print 'Longitude: ' + str(json_dict1[1][0]['longitude'])
print 'Latitude: ' + str(json_dict1[1][0]['latitude'])
print 'Iso2code: ' + str(json_dict1[1][0]['iso2Code'])