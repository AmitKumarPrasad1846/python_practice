# Here you can practice your practice code and erase it and if wanna add this code the use open_playground.py and save it there.

word = "learning"
with open("H_practice.txt", "r") as o:
    reading = o.read()

if (reading.find(word) != -1):
    print("found")
else:
    print("not found")