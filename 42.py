messagel = 'Peocessing file %s'
print(messagel % ('file_1.txt'))
message2 = 'File %s has size %d KB'
print(message2 % ('file_1.txt',100))
message3 = 'File %20s has size %10d KB'
print(message3 % ('file_1.txt',100))
message4 = 'Processing file {0:s}'
message4.format('file_1.txt')
print(message4)
message5 = 'File {0:s} has size {1:d}'
message5.format('file_1.txt',100)
print(message5)
spam=42
type(spam)

helloMessage = "Hello %s!"
print(helloMessage % ('Kate'))
print(helloMessage % ('Cris'))
helloMessage = "Hello {0:s}!"
helloMessage.format('Kate')
helloMessage.format('Chris')
helloMessage = "%s has %d %s"
print(helloMessage % ('Kate',1,'animal'))
print(helloMessage % ('Chris',1000,'$'))

line = "%20s costs %6d €"
print(line % ('ICE CREAM',3))