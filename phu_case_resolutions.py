 
'''
phu_case_resolutions.py
 Author(s): Matthew Parra (1105933), Joshua Komonen (1150389) , Sukhman Brar (1102371), Armaan Mattu (1149564)
 
 Project: Milestone III
 Date of Last Update: Mar 31, 2021.

 Commandline parameters: 3
     argv[0] = data file
     argv[1] = csv file
     argv[2] = start_date
     argv[3] = end_date
     argv[4] = PHU Number

 Compilation example: python phu_case_resolutions.py cases_by_status_and_phu.csv 2020-04-10 2020-05-25 2236 
 
 NOTE: Outputs total amount of resolved cases between the two dates (start date and end date) of a specific public health unit
 '''
 
import sys
import csv

def main(argv):

  if len(argv) != 5:
    print("Usage: cases_by_status_and_phu.py <file name> <start date> <end date> <phu number>")
    sys.exit(1)

  filename = argv[1]
  start_date = argv[2]
  end_date = argv[3]
  phuNum = argv[4]

  try:
    filename = open (filename, encoding="utf-8-sig")

  except IOError as err:
        print("Unable to open file '{}' : {}".format(
                filename, err), file=sys.stderr)
        sys.exit(1)

  data_reader = csv.reader(filename)

  dateList = []
  resolutions = []
  counter = 0
  resolutionNum = 0
  
  

  


  for row in data_reader:
    if start_date <= row[0] and phuNum == row[2]:
      if end_date < row[0]:
        break
      dateList.append(row[0])
      if row[4]:
        resolutionNum = int(row[4])
      resolutions.append(resolutionNum)
      

  print('Reported Date,Total Resolutions for {}'.format(phuNum))
  

  for x in dateList:
    print("{},{}".format(dateList[counter],resolutions[counter]))
    counter += 1
  


main(sys.argv)