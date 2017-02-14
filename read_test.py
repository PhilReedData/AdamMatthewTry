try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
import  json
import pprint

apiKey = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
url = "https://api.amdigital.co.uk/1.0/massobservation/documents?apiKey=" + apiKey + "&take=1"
response = urlopen(url)
data = json.loads(response.read())

pp = pprint.PrettyPrinter(indent=2)
#print data
pprint.pprint(data)

# import csv
# with open('mycsvfile.csv','wb') as f:
    # w = csv.writer(f)
    # w.writerow(data.keys())
    # w.writerow(data.values())