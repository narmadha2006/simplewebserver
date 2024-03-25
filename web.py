from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
<title>Top 5 Software Companies With Revenue</title>
</head>
<body bgcolor="cyan">
<table border="3" cellspacing="4" cellpadding="6" align="center" bgcolor="pink">
<caption>TOP FIVE REVENUE GENERATING SOFTWARE COMPANIES </caption>
             <tr>
               <th>Sno</th>
               <th>Company Name</th>
               <th>Revenue</th>
               <th>todays</th>
               <th>country</th>
          </tr>
           <tr>
               <td>01</td>
               <td>Microsoft</td>
               <td>$161 billion</td>
               <td>-1.18%</td>
               <td>USA</td>
          </tr>
          <tr>
               <td>02</td>
               <td>Oracle</td>
               <td>$48 billion</td>
               <td>-1.94%</td>
               <td>USA</td>
          </tr>
          <tr>
               <td>03</td>
               <td>Adobe</td>
               <td>$16 billion</td>
               <td>-1.54%</td>
               <td>USA</td>

          </tr>
          <tr>
               <td>04</td>
               <td>Salesforce</td>
               <td>$14 billion</td>
               <td>-1.86%</td>
               <td>USA</td>

          </tr>
          <tr>
               <td>05</td>
               <td>SAP</td>
               <td>$12 billion</td>
               <td>-1.46%</td>
               <td>USA</td>

          </tr>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()