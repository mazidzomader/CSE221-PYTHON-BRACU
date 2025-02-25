def modification(train_details):
    temp = train_details.split()
    name = temp[0]
    destination = temp[4]
    time = temp[6]
    return (name, destination, time, train_details)
def time_to_minute_converter(string):
    hour = int(string[0:2])
    minute = int(string[3:len(string)])
    return hour * 60 + minute
def unknown_stable_sort(data, n) :
    for i in range(n):
        for ii in range(n-i-1):
            if (data[ii][0] > data[ii + 1][0] or
                (data[ii][0] == data[ii + 1][0] and time_to_minute_converter(data[ii][2]) < time_to_minute_converter(data[ii + 1][2]))):
                data[ii], data[ii + 1] = data[ii + 1], data[ii]
    return data

n = int(input())
data = []
for i in range(n) :
    x = input()
    data.append(modification(x))
after_rearrangement = unknown_stable_sort(data,n)
for train in after_rearrangement:
    print(train[3])
