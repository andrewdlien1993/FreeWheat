import requests
from lxml import etree
from io import StringIO

while True:
    url = 'http://freewheat.gear.host/'
    s = requests.Session()
    tree = etree.parse(StringIO(s.get(url).text), etree.HTMLParser())

    vs = tree.xpath('//input[@name="__VIEWSTATE" or @id="__VIEWSTATE"]')[0].get('value')
    ev = tree.xpath('//input[@name="__EVENTVALIDATION" or @id="__EVENTVALIDATION"]')[0].get('value')
    vsg = tree.xpath('//input[@name="__VIEWSTATEGENERATOR"]')[0].get('value')
    number1 = int(tree.xpath('//span[@id="lblFirstNumber"]/text()')[0])
    number2 = int(tree.xpath('//span[@id="lblSecondNumber"]/text()')[0])
    answer = number1 * number2
    data = {
      '__VIEWSTATE': vs,
      '__VIEWSTATEGENERATOR': vsg,
      '__EVENTVALIDATION': ev,
      'txtAnswer': str(answer),
    }
    s.post(url, data=data, verify=False)
    print('{} x {} = {}'.format(number1, number2, answer))