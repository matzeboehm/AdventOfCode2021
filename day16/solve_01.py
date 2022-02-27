def unfold(bitpack):
    if len(bitpack) < 6: 
        return bitpack, 0
    
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
        lengthTypeID = remaining[0]
        remaining = remaining[1:]

        # 15 bits
        if lengthTypeID == "0":
            amountBits = int(remaining[0:15], 2)
            remaining = remaining[15:]

            subPackets = remaining[0:amountBits]
            
            decNum = 0
            while subPackets.count("0") != len(subPackets):
                subPackets, numberTemp = unfold(subPackets)
                decNum += numberTemp

            remaining = remaining[amountBits:]
            return remaining, decNum
        # 11 bits
        else:
            amountSubpackets = int(remaining[0:11], 2)
            remaining = remaining[11:]
            
            decNum = 0
            for i in range(amountSubpackets):
                remaining, numberTemp = unfold(remaining)
                decNum += numberTemp
            
            return remaining, decNum

with open("input.txt", "r") as file:
    hexinput = file.readline()
    decinput = int(hexinput, base = 16)
    bininput = str(bin(decinput))[2:]

    if len(bininput)%4 != 0:
        irrelevant, missing = divmod(len(bininput), 4)
        bininput = missing * "0" + bininput

    remaining = bininput[:]
    number = 0

    versionCounter = 0

    while remaining.count("0") != len(remaining):
        remaining, numberTemp = unfold(remaining)
        number += numberTemp

    #print(number)
    print(versionCounter)