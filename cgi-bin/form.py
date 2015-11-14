#!/usr/bin/env python3
import cgi
import html

form = cgi.FieldStorage()
text1 = html.escape(form.getfirst("TEXT_1", "undefined"))

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("{}".format(text1))

print("""</body>
        </html>""")