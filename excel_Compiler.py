import os
import csv

f = input('Enter file path of the parent folder containing the csv\'s: ')
name = input('Specify the name of the file to be written: ')
location = input("Specify the file location: ")

with open(location + '\\' + name + '.csv', "w") as csv_file:
    writer=csv.writer(csv_file, delimiter=",",lineterminator="\n")
    writer.writerow(["PebbleCounts"])
    writer.writerow([])
    writer.writerow(["UTM X (m)", "UTM Y (m)", "a (px)", "b (px)",
                     "a (m)", "b (m)", "area (px)", "area (m2)",
                     "orientation", "ellipse area (px)", "perc. diff. area"])
    writer.writerow([])
csv_file.close

for (root, dirs, files) in os.walk(f):
    for file in files:
        if file.endswith('.csv'):

            with open(root + '\\' + file, mode='r') as csv_file_root, open(location + '\\' + name + '.csv', "a") as csv_file:
                writer = csv.writer(csv_file, delimiter=",", lineterminator="\n")
                reader = csv.reader(csv_file_root, delimiter=',')

                #To eliminate the headers after each
                next(reader)
                next(reader)
                next(reader)
                next(reader)
                next(reader)
                next(reader)
                next(reader)
                next(reader)
                next(reader)
                next(reader)

                for line in reader:
                    writer.writerow(line)

                csv_file_root.close()
csv_file.close()

'''
TESTCASE:

C:\\Users\Mikey\Desktop\Clips\LC1\LC1Steep\LC1Steeptiles_ortho
LC1.steep
C:\\Users\Mikey\Desktop\Clips\LC1\LC1Steep

'''