with open("/content/sample_data/anscombe.json",'r') as my_file:
  json_data = json.load(my_file)

print(json_data)
type(json_data[0])
header=','.join(json_data[0].keys())
values_list =[]
for row_val in json_data:
  value=','.join([str(i) for i in row_val.values()])
  values_list.append(value)

print(values_list)
csv_data = header + "\n"
for i in values_list:
  csv_data = csv_data +i+"\n"

print(csv_data)
with open("/content/sample_data/anscombeconverted.csv",'w') as my_file:
  my_file.write(csv_data)