import nrf2401Plus

timelast = 0.0
freqency = 0

def figureSPICommandType(i):
    for key, value in nrf2401Plus.spiPacketLookupTable.items():
        if (i & value[0]) == key:
            return [key, value]


def lookupReg(val):
    return nrf2401Plus.registerAddresses[val]


def parseValues(line):
    items = line.split(',')
    time = float(items[0])
    mosi = int(items[2].split(':')[1].split(';')[0].strip().split('x')[1], 16)
    miso = int(items[2].split(':')[2].strip().split('x')[1], 16)
    return [time, mosi, miso]


def parseLine(line, lines=[], printLines=True, printFreq=False, printData=False):
    global timelast
    global freqency
    dataPayload = []
    spiCMDArr = []
    freq = 0
    reg = ''
    [time, mosi, miso] = parseValues(line)
    diff = time - timelast
    if diff > .000011:
        timelast = time
        spiCMDArr = figureSPICommandType(mosi)
        if spiCMDArr:
            if spiCMDArr[1][1] == "READ_REGISTER" or spiCMDArr[1][1] == "WRITE_REGISTER":
                reg = lookupReg(mosi & ~spiCMDArr[1][0])
                if reg == "RF_CH":
                    [a, freq, b] = parseValues(lines[1])
                    freqency = freq
            elif spiCMDArr[1][1] == "WRITE_TX_PAYLOAD":
                if freqency == 80:
                    for a in lines[1:5]:
                        [z, data, x] = parseValues(a)
                        dataPayload.append(data)
                else:
                    for a in lines[1:6]:
                        [z, data, x] = parseValues(a)
                        dataPayload.append(data)

    timelast = time
    if printFreq:
        if freq:
            return "freqency: {freq}\n".format(freq=freq)
    if printData:
        if dataPayload:
            return "data: " + ','.join([str(a) for a in dataPayload]) + '\n'
    if printLines:
        if spiCMDArr:
            return line.strip() + '-' + spiCMDArr[1][1] + '-' + reg + '\n'
        else:
            return line
