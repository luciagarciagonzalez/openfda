import http.server
import socketserver
import http.client
import json

IP = 'localhost'
PORT = 8000

class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        if self.path == "/":
            with open("finalsearch.html", "r") as f:
                message = f.read()
                self.wfile.write(bytes(message, "utf8"))

        if "searchDrug" in self.path:
            if '&' in self.path:
                list_drugs = []
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPSConnection("api.fda.gov")
                data = self.path.split("=")
                drug = data[1]
                limit = data[2]
                url = "/drug/label.json?search=active_ingredient:"+ drug + "=" + limit
                print(url)
                conn.request("GET", url, None, headers)
                r1 = conn.getresponse()
                drugs_raw = r1.read().decode("utf-8")
                conn.close()
                drugs = json.loads(drugs_raw)
                for i in range(len(drugs['results'])):
                    list_drugs.append(drugs['results'][i]['active_ingredient'][0])

                with open("code.html", "w") as f:
                    f.write("<!doctype html>" + "<html>" + "<body>" + "<ul>")
                    for element in list_drugs:
                        element_1 = "<li>" + element + "</li>" + "\n"
                        f.write(element_1)
                    f.write("</ul>" + "</body>" + "</html>")
                with open("code.html", "r") as f:
                    file = f.read()
                self.wfile.write(bytes(file, "utf8"))
            else:
                limit = 10
                list_drugs = []
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPSConnection("api.fda.gov")
                data = self.path.split("=")
                drug = data[1]
                url = "/drug/label.json?search=active_ingredient:" + drug + "=" + limit
                print(url)
                conn.request("GET", url, None, headers)
                r1 = conn.getresponse()
                drugs_raw = r1.read().decode("utf-8")
                conn.close()
                drugs = json.loads(drugs_raw)
                for i in range(len(drugs['results'])):
                    list_drugs.append(drugs['results'][i]['active_ingredient'][0])

                with open("code.html", "w") as f:
                    f.write("<!doctype html>" + "<html>" + "<body>" + "<ul>")
                    for element in list_drugs:
                        element_1 = "<li>" + element + "</li>" + "\n"
                        f.write(element_1)
                    f.write("</ul>" + "</body>" + "</html>")
                with open("code.html", "r") as f:
                    file = f.read()
                self.wfile.write(bytes(file, "utf8"))


        elif "searchCompany" in self.path:
            if '&' in self.path:
                list_company = []
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPSConnection("api.fda.gov")
                data = self.path.split("=")
                company = data[1]
                limit = data[2]
                url = "/drug/label.json?search=openfda.manufacturer_name:" + company + ("=") + limit
                print(url)
                conn.request("GET", url, None, headers)
                r1 = conn.getresponse()
                company_raw = r1.read().decode("utf-8")
                conn.close()
                companies = json.loads(company_raw)
                for i in range(len(companies['results'])):
                    list_company.append(companies['results'][i]["openfda"]['manufacturer_name'][0])
                with open("code.html", "w") as f:
                    f.write("<!doctype html>" + "<html>" + "<body>" + "<ul>")
                    for element in list_company:
                        element_1 = "<li>" + element + "</li>" + "\n"
                        f.write(element_1)
                    f.write("</ul>" + "</body>" + "</html>")
                with open("code.html", "r") as f:
                    file = f.read()
                self.wfile.write(bytes(file, "utf8"))
            else:
                limit = 10
                list_company = []
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPSConnection("api.fda.gov")
                data = self.path.split("=")
                company = data[1]
                url = "/drug/label.json?search=openfda.manufacturer_name:" + company + ("=") + limit
                print(url)
                conn.request("GET", url, None, headers)
                r1 = conn.getresponse()
                company_raw = r1.read().decode("utf-8")
                conn.close()
                companies = json.loads(company_raw)
                for i in range(len(companies['results'])):
                    list_company.append(companies['results'][i]["openfda"]['manufacturer_name'][0])
                with open("code.html", "w") as f:
                    f.write("<!doctype html>" + "<html>" + "<body>" + "<ul>")
                    for element in list_company:
                        element_1 = "<li>" + element + "</li>" + "\n"
                        f.write(element_1)
                    f.write("</ul>" + "</body>" + "</html>")
                with open("code.html", "r") as f:
                    file = f.read()
                self.wfile.write(bytes(file, "utf8"))
        elif "listDrugs" in self.path:
            if '&' in self.path:
                drug_list = []
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPSConnection("api.fda.gov")
                data = self.path.split("=")
                limit = data[1]
                url = "/drug/label.json?" + ("limit=") + limit
                print(url)
                print(url)
                conn.request("GET", url, None, headers)
                r1 = conn.getresponse()
                drug_raw = r1.read().decode("utf-8")
                conn.close()
                drugs = json.loads(drug_raw)
                print(drugs)
                for i in range(len(drugs['results'])):
                    try:
                        if 'openfda' in drugs['results'][i]:
                            drug_list.append(drugs['results'][i]['openfda']["brand_name"][0])
                    except KeyError:
                        drug_list.append('Unknown')


                with open("code.html", "w") as f:
                    f.write("<!doctype html>" + "<html>" + "<body>" + "<ul>")
                    for element in drug_list:
                        element_1 = "<li>" + element + "</li>" + "\n"
                        f.write(element_1)
                    f.write("</ul>" + "</body>" + "</html>")

                with open("code.html", "r") as f:
                    file = f.read()

                self.wfile.write(bytes(file, "utf8"))
            else:
                limit = 10
                drug_list = []
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPSConnection("api.fda.gov")
                data = self.path.split("=")
                url = "/drug/label.json?" + ("limit=") + limit
                print(url)
                print(url)
                conn.request("GET", url, None, headers)
                r1 = conn.getresponse()
                drug_raw = r1.read().decode("utf-8")
                conn.close()
                drugs = json.loads(drug_raw)
                print(drugs)
                for i in range(len(drugs['results'])):
                    try:
                        if 'openfda' in drugs['results'][i]:
                            drug_list.append(drugs['results'][i]['openfda']["brand_name"][0])
                    except KeyError:
                        drug_list.append('Unknown')

                with open("code.html", "w") as f:
                    f.write("<!doctype html>" + "<html>" + "<body>" + "<ul>")
                    for element in drug_list:
                        element_1 = "<li>" + element + "</li>" + "\n"
                        f.write(element_1)
                    f.write("</ul>" + "</body>" + "</html>")

                with open("code.html", "r") as f:
                    file = f.read()

                self.wfile.write(bytes(file, "utf8"))
        elif "listCompanies" in self.path:
            if '&' in self.path:
                companies_list = []
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPSConnection("api.fda.gov")
                data = self.path.split("=")
                limit = data[1]
                url = "/drug/label.json?" + "limit=" + limit
                print(url)
                conn.request("GET", url, None, headers)
                r1 = conn.getresponse()
                company_raw = r1.read().decode("utf-8")
                conn.close()
                companies = json.loads(company_raw)
                for i in range(len(companies['results'])):
                    try:
                        if "openfda" in companies['results'][i]:
                            companies_list.append(companies['results'][i]['openfda']["manufacturer_name"][0])
                    except KeyError:
                        companies_list.append("Unknown")

                with open("code.html", "w") as f:
                    f.write("<!doctype html>" + "<html>" + "<body>" + "<ul>")
                    for element in companies_list:
                        element_1 = "<li>" + element + "</li>" + "\n"
                        f.write(element_1)
                    f.write("</ul>" + "</body>" + "</html>")

                with open("code.html", "r") as f:
                    file = f.read()

                self.wfile.write(bytes(file, "utf8"))
            else:
                limit = 10
                companies_list = []
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPSConnection("api.fda.gov")
                data = self.path.split("=")
                url = "/drug/label.json?" + "limit=" + limit
                print(url)
                conn.request("GET", url, None, headers)
                r1 = conn.getresponse()
                company_raw = r1.read().decode("utf-8")
                conn.close()
                companies = json.loads(company_raw)
                for i in range(len(companies['results'])):
                    try:
                        if "openfda" in companies['results'][i]:
                            companies_list.append(companies['results'][i]['openfda']["manufacturer_name"][0])
                    except KeyError:
                        companies_list.append("Unknown")

                with open("code.html", "w") as f:
                    f.write("<!doctype html>" + "<html>" + "<body>" + "<ul>")
                    for element in companies_list:
                        element_1 = "<li>" + element + "</li>" + "\n"
                        f.write(element_1)
                    f.write("</ul>" + "</body>" + "</html>")

                with open("code.html", "r") as f:
                    file = f.read()

                self.wfile.write(bytes(file, "utf8"))





Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
        pass
httpd.server_close()
do_GET(self)