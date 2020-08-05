import re
import pandas as pd

#-------T-I-T-L-E-------/
#                       | 
# LHCO to CSV converter |
#                       |
# Github/GastonMazzei   |
#                       |
#-----------------------\
#-------I-N-D-E-X-------/
#                       |
#  1) Functions         |
#         .intro        |
#         .convert      |
#         .main         |
#                       |
#  2) __init__          |
#           .script     |
#            starter    |
#-----------------------\

def intro():
  mssg_0 = """
---------------------------------------------/
Hi! this is an ".LHCO" to ".csv" converter.  |
Use cases include data processing in Python  |
by loading the ".csv" as a pandas.DataFrame  |
---------------------------------------------|
output will be "OUTPUT.csv" in current folder|
---------------------------------------------\
                                      
Q: What is the input file? 

formats: 
  1. path/to/file.LHCO 
  2. file.LHCO            (if the file is in
                          the current folder)
.
..
...
"""
  print(mssg_0)
  input_name =  input("Please submit your answer: ")
  try: 
    LHCO = open(input_name,'r')
    return LHCO
  except FileNotFoundError: 
    import sys
    sys.exit(1)
    print('Wrong file name or path')
  return

def convert(v):
  pattern = re.compile('[\s]*([a-z\.\-0-9/#]+)',re.I)
  return re.findall(pattern, v)

def main(f,row_limiter=False)
  h = []
  # rl = row limiter  (OFF)
  if row_limiter:      #rl
    limit = N          #rl
    i = 0              #rl

  for line in f:
    h += [line]
    if row_limiter:     #rl
      i += 1            #rl 
      if i>limit: break #rl

  f.close()
  data = []
  data_aux = []
  for line in h:
    temp = convert(line)
    if temp[0]=='0': 
      data += [data_aux]
      data_aux = []
    else:
      data_aux += temp
  
  # Exclude events with more than "?"
  # different 'particles' involved
  # M = ?
  # or don't filter any case:
  #
  M = int(max([len(x) for x in data])/len(data[0]))  
  cols = []
  for x in range(M):
    cols += [y+f'_{x+1}' for y in data[0]]

  df = pd.DataFrame(data[1:], columns=cols)
  #
  # Finally Tidy Up
  for x in range(M):
    df[f'#_{x+1}'] = x+1
  df = df.fillna(0)

  # Should we kill dummy cols?

  # Should we set a verbose
  # flag and output info?

  df.to_csv('OUTPUT.csv',index=None)
  print('Success!')
  return

#
# should replace with __init__
main(intro())









