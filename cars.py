from datetime import datetime
def get_entry_exit_timings(inputlist):
   entry_dict = {}
   exit_dict = {}
   for i in inputlist:
     if "ENTRY" in i:
       entry_dict[i[0]] = i[2]
     else:
       exit_dict[i[0]] = i[2]
   entry_exit_timings = []
   entry_dict_keys = entry_dict.keys()
   for j in entry_dict_keys:
     if j in exit_dict:
        entry_exit_timings.append(entry_dict.get(j))
        entry_exit_timings.append(exit_dict.get(j))
   if len(entry_exit_timings) != 0:
     find_avg_max_min(entry_exit_timings)
def find_avg_max_min(entry_exit_timings):
  sum = 0
  diff_days_list = []
  diff_hour_list = []
  diff_min_list = []
  for i in range(0, len(entry_exit_timings), 2):
   entry = entry_exit_timings[i]
   exit = entry_exit_timings[i + 1]
   entry_date = entry.split(' ')[0]
   exit_date = exit.split(' ')[0]
   entry_timings = entry.split(' ')[1]
   exit_timings = exit.split(' ')[1]
   entry_hours = entry_timings.split(':')[0]
   entry_minutes = entry_timings.split(':')[1]
   exit_hours = exit_timings.split(':')[0]
   exit_minutes = exit_timings.split(':')[1]
   date_format = "%d-%m-%Y"
   a = datetime.strptime(entry_date, date_format)
   b = datetime.strptime(exit_date, date_format)
   delta = b - a
   diff_days_list.append(delta.days * 1440)
   diff_hour = int(exit_hours) - int(entry_hours)
   diff_hour_list.append(diff_hour * 60)
   diff_min = int(exit_minutes) - int(entry_minutes)
   diff_min_list.append(diff_min)
  max_min = []
  for j in range(0, len(diff_hour_list)):
   max_min.append(diff_days_list[j]+diff_hour_list[j] + diff_min_list[j])
  for h in range(0, len(diff_hour_list)):
   sum = sum + (diff_days_list[h] + 
  diff_hour_list[h] + diff_min_list[h])
  avg = sum / len(diff_min_list)
  print("Average time of cars taken is {} minutes".format(int(avg)))
  print("Maximum time a car spent between entry and exit is {} minutes".format(max(max_min)))
  print("Minimum time a car spent between entry and exit is {} minutes".format(min(max_min)))
def main():
  while True:
   try:
    size_of_dataset = int(input("Enter the size of the Datasets: "))
    break
   except ValueError:
    print('Size will be Integer Only')
    continue
  print("Enter Datasets: ") #TN01AB7765,ENTRY,23-11-2021 16:10
  each_string_list = []
  inputs = []
  for loop in range(size_of_dataset):
    a = input()
    new = ""
    for i in range(len(a)):
      if a[i] == ',':
        each_string_list.append(new)
        new = ""
      else:
        new += a[i]
    each_string_list.append(new)
    tup = tuple(each_string_list)
    inputs.append(tup)
    each_string_list.clear()
  get_entry_exit_timings(inputs)
main()