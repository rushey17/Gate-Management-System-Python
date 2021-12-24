Problem Statement:
You are provided with a dataset of a gate management system of a tech park. The data is collected for the entry and exits of cars. The data is provided in an array of tuples and can be for any time range. The tuple has a car number, entry or exit, and the time. E.g.

[("KA03ND7721", "ENTRY", "23-12-2021 13:00"), ("TN01AB7765", "ENTRY", "23-12-2021 13:05"), ("KA03ND7721", "EXIT", "23-12-2021 13:54"), ....]

Given this data, you will have to extract the following information:
a. Average time in minutes that a car has taken between entry and exit
b. Maximum time a car has spent between entry and exit
c. Minimum time a car has spent between entry and exit

Assumptions:
a. The data is sorted by time
b. There may be only entry or exit entries for a car as they may have entered before the start of the time period or not exited yet. You will have to ignore such entries.
c. The data can be across days.
d. Datetime format is "DD-MM-YYYY HH:mm"
