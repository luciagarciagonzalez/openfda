import http.server
import socketserver
import http.client
import json


PORT = 8000

class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        headers = {'User-Agent': 'http-client'}

        conn = http.client.HTTPSConnection("api.fda.gov")
        conn.request("GET", "/drug/label.json?limit=10", None, headers)
        r1 = conn.getresponse()
        print(r1.status, r1.reason)
        repos_raw = r1.read().decode("utf-8")
        conn.close()

        repos = json.loads(repos_raw)
        drugs = []
        intro = "<!doctype html>" + "\n" + "<html>" + "\n" + "<body>" + "\n" "<ol>" + "\n"
        end = "</ol>" + "\n" + "</body>" + "\n" + "</html>"

        for i in range(len(repos['results'])):
            drugs.append(repos['result'][i]['active_ingredient'][0])

        with open("drug.html", "w") as f:
            f.write(intro)
            for element in drugs:
                drugs_list = "<li>" + element + "<\li>" + "\n"
                f.write(drug_list)
            f.write(end)
        with open("drug.html","r") as f:
            drugs = f.read()

        self.wfile.write(bytes(message, "utf8"))
        return

Handler = http.server.SimpleHTTPRequestHandler
Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()