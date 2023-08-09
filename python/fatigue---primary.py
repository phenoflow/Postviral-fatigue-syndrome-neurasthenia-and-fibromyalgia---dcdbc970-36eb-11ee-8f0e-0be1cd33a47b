# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"Eu46011","system":"readv2"},{"code":"F286.12","system":"readv2"},{"code":"1040.0","system":"med"},{"code":"1042.0","system":"med"},{"code":"12411.0","system":"med"},{"code":"16561.0","system":"med"},{"code":"18073.0","system":"med"},{"code":"2237.0","system":"med"},{"code":"27877.0","system":"med"},{"code":"3361.0","system":"med"},{"code":"4364.0","system":"med"},{"code":"4546.0","system":"med"},{"code":"4657.0","system":"med"},{"code":"4698.0","system":"med"},{"code":"6190.0","system":"med"},{"code":"6552.0","system":"med"},{"code":"717.0","system":"med"},{"code":"7529.0","system":"med"},{"code":"9127.0","system":"med"},{"code":"9656.0","system":"med"},{"code":"97284.0","system":"med"},{"code":"98512.0","system":"med"},{"code":"98734.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('postviral-fatigue-syndrome-neurasthenia-and-fibromyalgia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["fatigue---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["fatigue---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["fatigue---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
