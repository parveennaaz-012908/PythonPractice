with open("/content/sample_data/anscombe.json",'r') as my_file:
  json_data = json.load(my_file)

print(json_data)

data_file = open ('data_file.csv','w')
csv_writer=csv.writer(data_file)

count =0
for json_cnt in json_data:
  if count==0:
    header=json_cnt.keys()
    csv_writer.writerow(header)
    count++1
  csv_writer.writerow(json_cnt.values())
print(data_file)
data_file.close()
