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

        elif "searchDrugs" in self.path:
            list_drugs = []
            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            data = self.path.strip("search?").split("&")
            drug = data[0].split("=")[1]
            limit = data[1].split("=")[1]
            url = "/drug/label.json?search=active_ingredient:"+ drug + "&" + "limit=" + limit
            print(url)
            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            drugs_raw = r1.read().decode("utf-8")
            conn.close()
            drugs = json.loads(drugs_raw)
            new_drugs = str(drugs)
            for i in range(len(new_drugs['results'])):
                if 'active_ingredient' in new_drugs['results'][i]:
                    list_drugs.append(new_drugs['results'][i]['active_ingredient'][0])
                else:
                    list_drugs.append("This index has no drug")
            with open("drug.html", "w") as f:
                for element in list_drugs:
                    element_1 = "<li>" + element + "</li>" + "\n"
                    f.write(element_1)
            with open("drug.html", "r") as f:
                file = f.read()
            self.wfile.write(bytes(new_drugs, "utf8"))

        elif "seachCompany" in self.path:
            list_company = []
            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            data = self.path.strip("search?").split("&")
            company = data[1].split("=")[1]
            url = "/drug/label.json?search=manufacturer_name:" + company
            print(url)
            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            company_raw = r1.read().decode("utf-8")
            conn.close()
            companies = json.loads(company_raw)
            new_companies = str(companies)
            for i in range(len(new_companies['results'])):
                if 'active_ingredient' in new_companies['results'][i]:
                    list_company.append(new_companies['results'][i]['manufacturer_name'][0])
                else:
                    list_company.append("This index has no drug")
            with open("drug.html", "w") as f:
                for element in list_company:
                    element_1 = "<li>" + element + "</li>" + "\n"
                    f.write(element_1)
            with open("drug.html", "r") as f:
                file = f.read()
            self.wfile.write(bytes(new_companies, "utf8"))
        elif "listDrugs" in self.path:
            drug_list = []
            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            data = self.path.strip("search?").split("&")
            drug = data[0].split("=")[1]
            url = "/drug/label.json?" + drug
            print(url)
            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            drug_raw = r1.read().decode("utf-8")
            conn.close()
            drugs = json.loads(drug_raw)
            new_drugs = str(drugs)
            for i in range(len(new_drugs['results'])):
                try:
                    if "openfda" in new_drugs["results"][i]:
                        drug_list.append(new_drugs['results'][i]['openfda']["brand_name"][0])
                except KeyError:
                    drug_list.append("Unknow")

            with open("drug.html", "w") as f:
                for element in list:
                    element_1 = "<li>" + element + "</li>" + "\n"
                    f.write(element_1)

            with open("drug.html", "r") as f:
                file = f.read()

            self.wfile.write(bytes(new_drugs, "utf8"))
        elif "listCompanies" in self.path:
            companies_list = []
            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            data = self.path.strip("search?").split("&")
            company = data[1].split("=")[1]
            url = "/drug/label.json?search=manufacturer_name:" + company
            print(url)
            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            company_raw = r1.read().decode("utf-8")
            conn.close()
            companies = json.loads(company_raw)
            new_companies = str(companies)
            for i in range(len(new_companies['results'])):
                try:
                    if "openfda" in new_companies["results"][i]:
                        companies_list.append(new_companies['results'][i]['openfda']["brand_name"][0])
                except KeyError:
                    companies_list.append("Unknow")

            with open("drug.html", "w") as f:
                for element in list:
                    element_1 = "<li>" + element + "</li>" + "\n"
                    f.write(element_1)
            with open("drug.html", "r") as f:
                file = f.read()

            self.wfile.write(bytes(new_companies, "utf8"))




Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
        pass
httpd.server_close()
do_GET(self)