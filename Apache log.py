from pprint import pprint

with open("access.log", "r") as file_pointer:
  lines = file_pointer.readlines()

import re
import sqlite3
con = sqlite3.connect("access.db")
cur = con.cursor()
cur.execute("CREATE TABLE access(ip, code, useragent)")
res = cur.execute("SELECT name FROM sqlite_master")
res.fetchone()
('access.db',)
res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
res.fetchone() is None
True

log_regex = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[.+\] \"[^\"]+\" (\d{3}) \d+"

access_data = []
for line in lines:
  data = re.findall(log_regex, line)[0]
  access_data.append(data)

ip_list = [ip for ip, status_code in access_data]
ip_count = {}

for ip in ip_list:
  if ip not in ip_count:
    ip_count[ip] = 1
  else:
    ip_count[ip] += 1

final_data = {}

for ip, status_code in access_data:
  final_data[ip] = {}

for ip, status_code in access_data:
  if status_code not in final_data[ip]:
    final_data[ip][status_code] = 1
  else:
    final_data[ip][status_code] += 1

import json

with open("access.json", "w") as json_file_pointer:
  json.dump(final_data, json_file_pointer)

pprint(final_data)