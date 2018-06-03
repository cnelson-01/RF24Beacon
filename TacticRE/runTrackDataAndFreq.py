import logicParser

fileLoc = 'untitled.csv'  # logic analyzer csv in hex format spi

f = open(fileLoc, 'r')
fo = open('resultsFreq.txt', 'w')

lines = f.readlines()
for index, line in enumerate(lines):
    if 'Time' not in line:
        parsed = logicParser.parseLine(line, lines=lines[index:index + 6], printFreq=True, printData=True, printLines=False)
        if parsed:
            fo.write(parsed)

fo.close()

# #parse out and print the frequencies
# f = open('resultsFreq.txt', 'r')
#
# freqs = []
# for line in f.readlines():
#     freqs.append(int(line.split(':')[1].strip()))
#
# resStr = ''
# count = 0
# for a in freqs:
#     if count == 15:
#         resStr += '\n'
#         count = 0
#     resStr += str(a) + ' '
#     count += 1
#
# print(resStr)
