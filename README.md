# ssrf_redirector

A simple http redirector based on python3 http.server.

```
# start 
python3 ssrf_redirector.py 8080 http://google.com

# access it then location to google.com
curl 127.0.0.1 

# access it with loc header below, then location to baidu.com
curl 127.0.0.1:5555  -H "loc: http://baidu.com"
```
