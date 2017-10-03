import sys

def stars(arr):
    for i in arr:
        for j in range(0, i):
            sys.stdout.write("*")
        print

def starsAndLetters(arr):
    for i in arr:
        if(type(i) is int):
            for j in range(0, i):
                sys.stdout.write("*")
        else:
            for j in range(0, len(i)):
                sys.stdout.write(i[0].lower())
        print

stars([4, 6, 1, 3, 5, 7, 25])
print
starsAndLetters([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])