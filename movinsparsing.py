#for documentation
#https://docs.python.org/3/library/re.html
#https://thepythonguru.com/python-regular-expression/
#https://www.truugo.com/edifact/d95b/movins/

import re
import time

start_time = time.time()

#uploading edi content

try:
   with open("movins.txt") as file:
      movins = file.readlines()
except:
   print("file not found")
   exit()   

#pattern keys and variables

ctnr_name_pattern = re.compile(4*"\w"+7*"\d")
podpattern = re.compile(3*"\w"+"\W\d\W"+5*"\w"+":")
nxt_pod_pattern = re.compile(5*"\w")
ctnr_location_pattern = re.compile(7*"\d")


ctnr_names = []
ctnr_locations = []
ctnr_nxt_pod = []
i = 0

#backend
while i < len(movins):

   match_ctnr_pod = re.search(podpattern, movins[i])
   i += 1
   if match_ctnr_pod and match_ctnr_pod.group() == "LOC+9+MAMED:":

      for j in range(i,-1,-1):
            match_ctnr_pos = re.search(ctnr_location_pattern, movins[j])
            if match_ctnr_pos:
               ctnr_locations.append(match_ctnr_pos.group())
               break

      match_nxt_pod = re.search(nxt_pod_pattern, movins[i])

      if match_nxt_pod:
         for j in range(i+1, len(movins)):
            match_ctnr_name = re.search(ctnr_name_pattern, movins[j])
            if match_ctnr_name:
               ctnr_names.append(match_ctnr_name.group())
               ctnr_nxt_pod.append(match_nxt_pod.group())
               i = j+1
               break

#output

for i in range(len(ctnr_names)):
   print(str(ctnr_names[i])+' '+str(ctnr_nxt_pod[i])+' '+str(ctnr_locations[i]))

print("--- %s seconds to run ---" % (time.time() - start_time))
