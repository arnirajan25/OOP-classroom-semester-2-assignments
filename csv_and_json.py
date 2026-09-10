import csv
import json

students = [
    {"roll_number":1,"name":"Aakriti Shrestha","address":"Baneshwor, Kathmandu"},
    {"roll_number":2,"name":"Amos Tamang","address":"Koteshwor, Kathmandu"},
    {"roll_number":3,"name":"Anjina Shrestha","address":"Boudha, Kathmandu"},
    {"roll_number":4,"name":"Ayush Gole","address":"Kalanki, Kathmandu"},
    {"roll_number":5,"name":"Biplob Raj Kunwar","address":"Swayambhu, Kathmandu"},
    {"roll_number":6,"name":"Dipa Rimal","address":"Chabahil, Kathmandu"},
    {"roll_number":7,"name":"Karuna Bista","address":"Kirtipur, Kathmandu"},
    {"roll_number":8,"name":"Mahim Mashrangi Magar","address":"Gongabu, Kathmandu"},
    {"roll_number":9,"name":"Manjil Kuinkel","address":"Thamel, Kathmandu"},
    {"roll_number":10,"name":"Nirajan Aryal","address":"Sinamangal, Kathmandu"},
    {"roll_number":11,"name":"Prabisha Shrestha","address":"Jorpati, Kathmandu"},
    {"roll_number":12,"name":"Pradip Khanal","address":"Budhanilkantha, Kathmandu"},
    {"roll_number":13,"name":"Prashamsha Adhikari","address":"Sundarijal, Kathmandu"},
    {"roll_number":14,"name":"Rajib Shrestha","address":"Baluwatar, Kathmandu"},
    {"roll_number":15,"name":"Rojan Timalsina","address":"Maharajgunj, Kathmandu"},
    {"roll_number":16,"name":"Rustam Pandit","address":"Naxal, Kathmandu"},
    {"roll_number":17,"name":"Safal Shrestha","address":"Tokha, Kathmandu"},
    {"roll_number":18,"name":"Sudip Gurung","address":"Chandragiri, Kathmandu"},
    {"roll_number":19,"name":"Suhag Adhikari","address":"Balaju, Kathmandu"},
    {"roll_number":20,"name":"Sujan Yokpangden","address":"Gaushala, Kathmandu"},
    {"roll_number":21,"name":"Sushil Rumba","address":"Dillibazar, Kathmandu"},
    {"roll_number":22,"name":"Yunish Gurung","address":"Bouddha Stupa Road, Kathmandu"}
]

csv_filename = "students.csv"
json_filename = "students.json"

with open(csv_filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["roll_number", "name", "address"])
    writer.writeheader()
    writer.writerows(students)
print(f"Created {csv_filename} with {len(students)} records.")

for s in students:
    print(f"Roll No: {s['roll_number']:<3} Name: {s['name']:<25} Address: {s['address']}")

with open(csv_filename, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = [dict(row, roll_number=int(row["roll_number"])) for row in reader]

with open(json_filename, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
print(f"\nConverted {csv_filename} -> {json_filename} ({len(data)} records).\n")
print(f"Contents of {json_filename}:")
print(json.dumps(data, indent=4))
