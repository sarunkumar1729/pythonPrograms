import csv

with open('contacts.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    vcf_contacts = []
    for row in csv_reader:
        name = row['name']+' AG'
        phone = row['phone']
        vcf_contacts.append(f'BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL:{phone}\nEND:VCARD')

with open('contacts.vcf', 'w') as vcf_file:
    for vcard in vcf_contacts:
        vcf_file.write(vcard + '\n')

