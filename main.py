import requests as rq
import xml.etree.ElementTree as et

degree = '-3'

url = 'https://www.w3schools.com/xml/tempconvert.asmx'

SOAPEnvelope = f"""
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <CelsiusToFahrenheit xmlns="https://www.w3schools.com/xml/">
      <Celsius>{degree}</Celsius>
    </CelsiusToFahrenheit>
  </soap:Body>
</soap:Envelope>
"""

options = {"Content-Type": "text/xml; charset=utf-8"}

response = rq.post(url, data=SOAPEnvelope, headers=options)
root = et.fromstring(response.text)

for child in root.iter("{https://www.w3schools.com/xml/}CelsiusToFahrenheitResult"):
    print(child.text)
