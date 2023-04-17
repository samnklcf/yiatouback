import http.client

conn = http.client.HTTPSConnection("127.0.0.1", 8000)

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
}

payload = ""

conn.request("POST", "/api/token", payload, headersList)
response = conn.getresponse()
result = response.read()

print(result.decode("utf-8"))