#!/usr/bin/python3
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import control_in_stock

#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>add_cart</title>
</head>
<body>
""")

form = cgi.FieldStorage()



id_amount = form.getvalue(f'amount')
id_price = form.getvalue(f'price')
id_name = form.getvalue(f'name')
status = control_in_stock.addProduct(id_name, id_price, id_amount)
if(status == False):
    print("資料不齊全，未成功新增")

    
    
print("新增完成")
print("<br><a href='root.py'>查看管理頁面</a>")
print("<br><a href='orderList.py'>查看訂單</a>")
print("</body></html>")
