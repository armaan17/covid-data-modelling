#!/usr/bin/env python
 
'''
read_names.py
 Author(s): Matthew Parra (1105933), Joshua Komonen (1150389) , Sukhman Brar (1102371), Armaan Mattu (1149564)
 
 Project: Milestone III
 Date of Last Update: Mar 31, 2021.

 Commandline parameters: 3
     argv[0] = data file
     argv[1] = csv file
     argv[2] = date

 Compilation example: python individuals_vaccinated_over_time.py vaccine_doses.csv 2021-02-01
 
 '''
 
import sys
import csv

def main(argv):

  if len(argv) != 3:
    print("Usage: individuals_vaccinated_over_time.py <file name> <end date>")
    sys.exit(1)

  filename = argv[1]
  end_date = argv[2]

  try:
    filename = open (filename, encoding="utf-8-sig")

  except IOError as err:
        print("Unable to open file '{}' : {}".format(
                filename, err), file=sys.stderr)
        sys.exit(1)

  data_reader = csv.reader(filename)

  dateList = []
  fullVac = []
  counter = 1

  


  for row in data_reader:
    tempList = row[0]
    if end_date != tempList:
      dateList.append(row[0])
      if row[4]: #if anything on row @ index 4
        item = row[4]
        item = item.replace(",", "") #replace comma with nothing
        fullVac.append(item)
      else:
        fullVac.append(0) #if not just put 0
    else:
      dateList.append(row[0])
      fullVac.append(row[4].replace(",", ""))
      break

  print('Reported Date, Total Individuals Fully Vaccinated')

  while counter < len(dateList):
    print("{},{}".format(dateList[counter], fullVac[counter]))
    counter += 1

main(sys.argv)
