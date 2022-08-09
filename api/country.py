from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    query_dict = dict(parse.parse_qsl(parse.urlsplit(self.path).query))

    if "name" in query_dict:
      url = "https://restcountries.com/v3.1/name/"
      response = requests.get(url + query_dict["name"])
      data = response.json()
      country = data[0]['name']['common']
      capital = data[0]["capital"][0]
      message = str(f"The capital of {country} is {capital}.")
    else:
      message = "Enter a country!"

    self.wfile.write(message.encode())
    return
