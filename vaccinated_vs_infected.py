#!/usr/bin/env python
 
'''
read_names.py
 Author(s): Matthew Parra (1105933), Joshua Komonen (1150389) , Sukhman Brar (1102371), Armaan Mattu (1149564)
 
 Project: Milestone III
 Date of Last Update: Mar 31, 2021.

 Commandline parameters: 3
     argv[0] = data file
     argv[1] = csv file 1
     argv[2] = csv file 2
     argv[3] = start date
     argv[4] = end date

 Compilation example: python vaccinated_vs_infected.py vaccine_doses.csv conposcovidloc.csv 2020-12-24 2021-01-21
 
 '''
 
import sys
import csv

def main(argv):

  if len(argv) != 5:
    print("Usage: individuals_vaccinated_over_time.py <file name> <file name 2> <start date> <end date>")
    sys.exit(1)

  filename1 = argv[1]
  filename2 = argv[2]
  start_date = argv[3]
  end_date = argv[4]

  try:
    filename1 = open (filename1, encoding="utf-8-sig")
    filename2 = open (filename2, encoding="utf-8-sig")

  except IOError as err:
        print("Unable to open file '{}' or '{}' : {}".format(
                filename1, filename2, err), file=sys.stderr)
        sys.exit(1)

  data_reader = csv.reader(filename1)
  data_reader2 = csv.reader(filename2)

  dateList = []
  infectedDate = []
  infectedTotal = []
  totalInfected = 0
  numInfected = 0
  fullVac = []
  counter = 0
  

  next(data_reader)
  for row in data_reader: 
    if start_date <= row[0]:
      if end_date < row[0]:
        break
      dateList.append(row[0])
      if row[4]:
        item = row[4]
        item = item.replace(",", "") #replace comma with nothing
        fullVac.append(item)
      else:
        fullVac.append(0)
  
  tempDate = ""
  next(data_reader2)
  for row in data_reader2:
    if row[1] == tempDate:
      numInfected += 1
    tempDate = row[1]
    if start_date <= tempDate:
      if end_date < tempDate:
        break
      infectedDate.append(tempDate)
      totalInfected += numInfected
      infectedTotal.append(totalInfected)
  
  print('Reported Date, Total Individuals Fully Vaccinated, Total Individuals Infected')
  
  for x in dateList:
    print("{},{},{}".format(dateList[counter], fullVac[counter], infectedTotal[counter]))
    counter += 1

main(sys.argv)