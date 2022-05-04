import time
secs = 0
pen = 0
nic = 0
quart = 0
doll = 0
totalSec = 0

try:
    totalSec = int(input("How Many Seconds Would You Like?: "))
except:
    print("Please Input a Variable")

for n in range(totalSec):
    # Counts the seconds
    print("Seconds")
    secs += 1
    print(secs)
    print(" ")
    pen += 1
    # Prints the coin counts
    print(f"Pennies {pen}")
    print(f"Nickles {nic}")
    print(f"Quarters {quart}")
    print(f"Dollars {doll}")
    print(" ")
    time.sleep(1)

    if pen == 5:
        nic += 1
        pen -= 5

    if nic == 5:
        quart += 1
        nic -= 5

    if quart == 4:
        doll += 1
        quart -= 4

# Final Count Check
if pen == 5:
    nic += 1
    pen -= 5

if nic == 5:
    quart += 1
    nic -= 5

if quart == 4:
    doll += 1
    quart -= 4

