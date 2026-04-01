import random

# Taking input
flag = "FLAG{" + input("flag:") + "}"
length = len(flag)

for i in range(int(input("copys:"))):

    # Generating key
    key = random.sample(range(3, (length+1) * 3, 3), length)

    # Encoding Flag
    temFlag = list(flag)
    for x in range(length):
        temFlag[x] = (ord(temFlag[x]) * key[x]) % 256
    print(temFlag)
