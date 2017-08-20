from urllib.request import urlopen
import xml.etree.ElementTree as et
import json

def get_loc():
    url = "http://weather.livedoor.com/forecast/rss/primary_area.xml"
    response = urlopen(url)
    data = response.read()
    root = et.fromstring(data)
    loc = {}
    for pref in root[0].find('{http://weather.livedoor.com/%5C/ns/rss/2.0}source'):
        for city in pref.findall("city"):
            loc[city.attrib['title']] = int(city.attrib['id'])
    return loc

loc = get_loc()
def forecast(city):
    url = "http://weather.livedoor.com/forecast/webservice/json/v1?city=" + f'{city:06d}'
    response = urlopen(url)
    content = json.loads(response.read().decode("utf8"))
    print(content['title'])
    print(content['description']['text'])
    print()
    for forecast in content['forecasts']:
        dateLabel = forecast['dateLabel']
        date = forecast['date']
        telop = forecast['telop']
        if forecast['temperature']['min'] != None:
            tmin = forecast['temperature']['min']['celsius']
        else:
            tmin = "--"
        if forecast['temperature']['max'] != None:
            tmax = forecast['temperature']['max']['celsius']
        else:
            tmax = "--"
        print(f"{dateLabel:　<3}（{date}）{telop:　<7}{tmin:>3}{tmax:>3}")
