import json
import csv

json_list = []
json_list.clear()
json_list = []

#open JSON file
with open('employees.json') as json_file:
    data = json.load(json_file)
    for i in data:
        if i['totp_enabled'] == False:
            json_list.append(i)  

#add manager key to dictionary
count2 = 0
for i in json_list:
    json_list[count2]['manager'] = ""
    count2 += 1

csv_list = []
csv_list.clear()
csv_list = []
# Open CSV file
with open('engineering.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)
    for row in csv_reader:
        row_data = {key: value for key, value in zip(headers, row)}
        csv_list.append(row_data)

count4 = 0
for i in json_list:
    ej = json_list[count4]["email"]
    count5 = 0
    for i in csv_list:
        ec = csv_list[count5]["email"]
        if ej == ec:
            json_list[count4]["manager"] = csv_list[count5]["manager"]
        count5 += 1
    count4 +=1

json_list2 = []
json_list2.clear
json_list2 = []
count1 = 0
for i in json_list:
    if i["manager"] != "":
        json_list2.append(i)
        json_list2[count1].pop("totp_enabled") 
        count1+=1

fieldnames = ['firstName', 'lastName', 'email','username', 'jobTitle', 'manager']
with open('results.csv', 'w', newline='') as testfile:
    csv_writer = csv.DictWriter(testfile, fieldnames = fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(json_list2)