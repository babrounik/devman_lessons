# Bitly url shorterer

This script gets a link. 
If it is a bitly link then it returns amount of clicks.
It it is an usual link then it returns shorted link. 

### How to install
To run script you have to be in the same directory where it is. Or run python with full file path.

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Examples
How to short link:
```
(env) A:\Projects\devman\proj>python api_lesson_2.py -l https://google.com
>>> DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): api-ssl.bitly.com:443
>>> DEBUG:urllib3.connectionpool:https://api-ssl.bitly.com:443 "POST /v4/shorten HTTP/1.1" 200 264
>>> INFO:root:https://bit.ly/2CCtscC
```
How to get clicks:
```
(env) A:\Projects\devman\proj>python api_lesson_2.py -l bit.ly/2CCtscC
>>> DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): api-ssl.bitly.com:443
>>> DEBUG:urllib3.connectionpool:https://api-ssl.bitly.com:443 "GET /v4/bitlinks/bit.ly/2CCtscC/clicks/summary?unit=day&units=-1 HTTP/1.1" 200 83
>>> INFO:root:{'unit_reference': '2020-08-02T12:36:10+0000', 'total_clicks': 1, 'units': 30, 'unit': ''}
```