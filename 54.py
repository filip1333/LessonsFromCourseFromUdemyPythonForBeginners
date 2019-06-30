s='A Python script'
print(s[0])
print(s[2])
print(s[2:7])
print(s[2:8])
print(s[:8])
print(s[8:])
print(s[2:999])
print(s[99:999])

message = 'Document "cv.doc" was printer: XEROX'
print(message.find(':'))
print(message[29:9999])
print(message[message.find(':')+2:])
print(message[message.find('"')+1:])
tmp = message[message.find('"')+1:]
print(tmp[:tmp.find('"')])

q = "THE EYES"
print(q[0],q[1],q[2],q[5],q[3],q[7],q[4],q[6])
print(q[0]+q[1]+q[2]+q[5]+q[3]+q[7]+q[4]+q[6])

q = 'a gentleman'
print(q[3],q[6],q[7],q[2],q[0],q[4],q[5],q[1],q[8:])
print(q[3]+q[6]+q[7]+q[2]+q[0]+q[4]+q[5]+q[1]+q[8:])

q = "THE MORSE CODE"
print(q[1:3],q[6],q[8],q[3],q[10:12],q[4],q[13],q[9],q[12],q[5],q[0],q[7])
print(q[1:3]+q[6]+q[8]+q[3]+q[10:12]+q[4]+q[13]+q[9]+q[12]+q[5]+q[0]+q[7])

line = 'Program "Kropka nad i" nadamy o: 20:00'
time = line[line.find(':')+2:]
print(time)
tmp = line[line.find('"'):]
print(tmp)
title = tmp[:tmp.find('"')]
print(tmp[:tmp.find('"')])
print(title)
print(time)