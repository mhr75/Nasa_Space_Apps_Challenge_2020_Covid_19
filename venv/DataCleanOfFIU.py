import csv
with open ('cln_txt_DOT.csv',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['user_id'])