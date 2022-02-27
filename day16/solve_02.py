from operator import add, mul, gt, lt, eq

def operation(opsID, decNumList):
    ops = [add, mul, lambda *x: min(x), lambda *x: max(x), None, gt, lt, eq]

    res = decNumList[0]
    for i in range(len(decNumList) - 1):
        res = ops[opsID](res, decNumList[i+1])
    return res

def unfold(bitpack):
    packetVersion = int(bitpack[0:3], 2)
    packetID = int(bitpack[3:6], 2)

    global versionCounter
    versionCounter += packetVersion

    remaining = bitpack[6:]

    # literal
    if packetID == 4:
        binNumber = ""
        while True:
            trailing = remaining[0]
            binNumber += remaining[1:5]
            remaining = remaining[5:]
            # not last group
            if trailing == "1":
                pass
            # last group
            else:
                break
            
        numberDec = int(binNumber, 2)
        return remaining, numberDec
    
    # operation
    else:
        ops = [add, mul, lambda *x: min(x), lambda *x: max(x), None, gt, lt, eq]
        opsID = packetID

        lengthTypeID = remaining[0]
        remaining = remaining[1:]
        
        decNumList = []

        # 15 bits
        if lengthTypeID == "0":
            amountBits = int(remaining[0:15], 2)
            remaining = remaining[15:]

            subPackets = remaining[0:amountBits]
            
            while subPackets.count("0") != len(subPackets):
                subPackets, numberTemp = unfold(subPackets)
                decNumList.append(numberTemp)

            decNum = operation(opsID, decNumList)
            remaining = remaining[amountBits:]
            return remaining, decNum
        # 11 bits
        else:
            amountSubpackets = int(remaining[0:11], 2)
            remaining = remaining[11:]
            
            for i in range(amountSubpackets):
                remaining, numberTemp = unfold(remaining)
                decNumList.append(numberTemp)    

            decNum = operation(opsID, decNumList)
            return remaining, decNum

with open("input.txt", "r") as file:
    hexinput = file.readline()
    decinput = int(hexinput, base = 16)
    bininput = str(bin(decinput))[2:]

    if len(bininput)%8 != 0:
        irrelevant, missing = divmod(len(bininput), 8)
        bininput = (8 - missing) * "0" + bininput

    versionCounter = 0

    remaining, number = unfold(bininput)
    
    print("Task 1: %i" %(versionCounter))
    print("Task 2: %i" %(number))