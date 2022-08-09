from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    query_dict = dict(parse.parse_qsl(parse.urlsplit(self.path).query))

    if "capital" in query_dict:
      url = "https://restcountries.com/v3.1/capital/"
      response = requests.get(url + query_dict["capital"])
      data = response.json()
      country = data[0]['name']['common']
      capital = data[0]["capital"][0]
      message = str(f"{capital} is the capital of {country}.")
    else:
      message = "Enter a capital!"


    self.wfile.write(message.encode())
    return
