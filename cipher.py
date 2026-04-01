import random

# Taking input
flag = "FLAG{" + input("flag:") + "}"
length = len(flag)

for i in range(int(input("copys:"))):

    # Generating key
    key = random.sample(range(1, (length+1) * 3, 3), length)

    # Encoding Flag
    temFlag = list(flag)
    for x in range(length):
        temFlag[x] = ord(temFlag[x]) * key[x]
    print(temFlag)
