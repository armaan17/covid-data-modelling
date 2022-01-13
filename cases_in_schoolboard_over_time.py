#!/usr/bin/env python
 
'''
read_names.py
 Author(s): Matthew Parra (1105933), Joshua Komonen (1150389) , Sukhman Brar (1102371), Armaan Mattu (1149564)
 
 Project: Milestone III
 Date of Last Update: Mar 31, 2021.

 Commandline parameters: 3
     argv[0] = data file
     argv[1] = csv file
     argv[2] = start_date
     argv[3] = end_date
     argv[4] = municipality

 Compilation example: python cases_in_schoolboard_over_time.py schoolpartnersactivecovid.csv 2020-09-16 2021-03-10 Brampton 
 
 NOTE: Outputs total amount of cases between the two dates(start date and end date)
 '''
 
import sys
import csv

def main(argv):

  if len(argv) != 5:
    print("Usage: cases_in_schoolboard_over_time.py <file name> <end date>")
    sys.exit(1)

  filename = argv[1]
  start_date = argv[2]
  end_date = argv[3]
  municipality = argv[4]

  try:
    filename = open (filename, encoding="utf-8-sig")

  except IOError as err:
        print("Unable to open file '{}' : {}".format(
                filename, err), file=sys.stderr)
        sys.exit(1)

  data_reader = csv.reader(filename)

  dateList = []
  cases = []
  counter = 0
  caseNum = 0
  
  

  


  for row in data_reader:
    if start_date <= row[0] and municipality == row[3]:
      if end_date < row[0]:
        break
      dateList.append(row[0])
      if row[4]:
        caseNum += int(row[4])
      cases.append(caseNum)
      

  print('Reported Date,Total Cases for {}'.format(municipality))
  

  for x in dateList:
    print("{},{}".format(dateList[counter],cases[counter]))
    counter += 1
  


main(sys.argv)
