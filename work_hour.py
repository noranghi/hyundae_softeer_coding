import sys

days = 5
minute = 0

for i in range(days):

    come,out = map(str, input().split())
    in_list = come.split(':')
    out_list= out.split(':')
    time = 0

    in_zero = int(in_list[0])
    in_first = int(in_list[1])

    out_zero = int(out_list[0])
    out_first = int(out_list[1])

    if int(out_first) >= int(in_first):
        time = ((out_zero-in_zero)*60)+(out_first-in_first)
        minute += time
    else:
        time = ((out_zero-1-in_zero)*60) + (out_first + 60 - in_first)
        minute += time

print(minute)