#Emily Pedrazzi
#WFQ
#CS 162
#4-20-2024

#Defining queues
P = []
S = []
E = []

#Dequeue packets function - used in loop
def dequeue(qname):
    num_packets = len(qname)
    return qname[:num_packets],qname[num_packets:]

#Splitting data into queues
with open("input queue-1-1.txt") as data_list:
    for data in data_list:
        priority = data[0]

        if(priority == "P"):
            P.append(data[2:-1])
        elif(priority == "S"):
            S.append(data[2:-1])
        else:
            E.append(data[2:-1])

#Loop condition
while any([P,S,E]):
    if P:
        Premium, P = dequeue(P)
        print("Premium:",Premium)
    if S:
        Standard, S = dequeue(S)
        print("Standard:",Standard)
    if E:
        Economy, E = dequeue(E)
        print("Economy:",Economy)

print("Premium:",P)
print("Standard:",S)
print("Economy:",E)
print("All queues are empty.")