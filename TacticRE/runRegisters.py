import logicParser

fileLoc = 'untitled.csv'  # logic analyzer csv in hex format spi

f = open(fileLoc, 'r')
fo = open('results.txt', 'w')


lines = f.readlines()
for index, line in enumerate(lines):
    if 'Time' not in line:
        parsed = logicParser.parseLine(line, lines=lines[index:index + 5])
        if parsed:
            fo.write(parsed)
