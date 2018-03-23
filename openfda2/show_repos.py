import http.client #they are libraries
import json

headers = {'User-Agent': 'http-client'}

#I have change the api of the teacher by my api
conn = http.client.HTTPSConnection("api.fda.gov")
conn.request("GET", "/users/luciagarciagonzalez/repos", None, headers)
r1 = conn.getresponse()
print(r1.status, r1.reason)
repos_raw = r1.read().decode("utf-8")
conn.close()

repos = json.loads(repos_raw)

