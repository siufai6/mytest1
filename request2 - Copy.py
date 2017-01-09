import grequests  

# dummy changes added

urls =["http://nominatim.openstreetmap.org/?format=json&q=[bakery]+berlin+wedding&format=json&limit=1",
"http://nominatim.openstreetmap.org/?format=json&q=15+Wong+Nei+Chung+Road+Happy+Valley&format=json&limit=1",
"http://nominatim.openstreetmap.org/?format=json&q=62-02+Fresh+Pond+Road+New+York&format=json&limit=1",
"http://nominatim.openstreetmap.org/?format=json&q=5717+Queens+Blvd+New+York&format=json&limit=1",
"http://nominatim.openstreetmap.org/?format=json&q=9015+Queens+Blvd+New+York+&format=json&limit=1",
"http://nominatim.openstreetmap.org/?format=json&q=3042+Steinway+Street+New+York+&format=json&limit=1",
"http://nominatim.openstreetmap.org/?format=json&q=8715+Northern+Blvd+New+York+&format=json&limit=1",
"http://nominatim.openstreetmap.org/?format=json&q=1286+Broadway+New+York+&format=json&limit=1",
"http://nominatim.openstreetmap.org/?format=json&q=One+Penn+Plaza+New+York+&format=json&limit=1",
"http://nominatim.openstreetmap.org/?format=json&q=761+Seventh+Avenue+New+York+&format=json&limit=1",
"http://nominatim.openstreetmap.org/?format=json&q=12114+Liberty+Avenue+New+York+&format=json&limit=1",
"http://nominatim.openstreetmap.org/?format=json&q=2755+Broadway+New+York+&format=json&limit=1",
"http://nominatim.openstreetmap.org/?format=json&q=707+Lenox+Ave.+New+York+&format=json&limit=1",
"http://nominatim.openstreetmap.org/?format=json&q=3645+Broadway+New+York+&format=json&limit=1",
"http://nominatim.openstreetmap.org/?format=json&q=1312+Beach+Channel+Drive+New+York+&format=json&limit=1",
"http://nominatim.openstreetmap.org/?format=json&q=152+Rockaway+Blvd.+New+York+&format=json&limit=1",
"http://nominatim.openstreetmap.org/?format=json&q=3647+Broadway+New+York+&format=json&limit=1"]

urls=['http://localhost:8080/app2/test.jsp',
'http://localhost:8080/app2/test.jsp',
'http://localhost:8080/app2/test.jsp',
'http://localhost:8080/app2/test.jsp',
'http://localhost:8080/app2/test.jsp',
'http://localhost:8080/app2/test.jsp',
'http://localhost:8080/app2/test.jsp',
'http://localhost:8080/app2/test.jsp',
'http://localhost:8080/app2/test.jsp',
'http://localhost:8080/app2/test.jsp',
'http://localhost:8080/app2/test.jsp'
]
    
def is_available(response, *args, **kwargs):  
    print(response.url, response.content)
    
def show_data(response, *args, **kwargs):  
    print(response.url, 'content is:', r.content )


#post_data = "this is a test of post"  
unsent_request = [grequests.get(url, hooks={'response': is_available})  for url in urls]
#grequests.post('http://httpbin.org//post', hooks={'response': is_available}, data=post_data)]  
resp=grequests.map(unsent_request)
print(resp)


print('done')