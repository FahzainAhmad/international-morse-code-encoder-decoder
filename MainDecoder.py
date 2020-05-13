# Author :cybersoul.exe
# 23/03/20

# A dict for decode
dic = {}

# entering values in dict
dic["A"] = "._"
dic["B"] = "_..."
dic["C"] = "_._."
dic["D"] = "_.."
dic["E"] = "."
dic["F"] = ".._."
dic["G"] = "__."
dic["H"] = "...."
dic["I"] = ".."
dic["J"] = ".___"
dic["K"] = "_._"
dic["L"] = "._.."
dic["M"] = "__"
dic["N"] = "_."
dic["O"] = "___"
dic["P"] = ".__."
dic["Q"] = "__._"
dic["R"] = "._."
dic["S"] = "..."
dic["T"] = "_"
dic["U"] = ".._"
dic["V"] = "..._"
dic["W"] = ".__"
dic["X"] = "_.._"
dic["Y"] = "_.__"
dic["Z"] = "__.."

# A dict for encode
endict = {}

# entering values in dict
endict["._"] = "A"
endict["_..."] = "B"
endict["_._."] = "C"
endict["_.."] = "D"
endict["."] = "E"
endict[".._."] = "F"
endict["__."] = "G"
endict["...."] = "H"
endict[".."] = "I"
endict[".___"] = "J"
endict["_._"] = "K"
endict["._.."] = "L"
endict["__"] = "M"
endict["_."] = "N"
endict["___"] = "O"
endict[".__."] = "P"
endict["__._"] = "Q"
endict["._."] = "R"
endict["..."] = "S"
endict["_"] = "T"
endict[".._"] = "U"
endict["..._"] = "V"
endict[".__"] = "W"
endict["_.._"] = "X"
endict["_.__"] = "Y"
endict["__.."] = "Z"

# empty string for decode
d = ""

# Just an important note
print("Enter in block(capital) letters")

# Get encode or decode
mui = input("Encode or Decode? :-")

# empty string for encode
e = ""

# main code for encode
if mui == "E" or mui == "encode" or mui == "Encode":
    while True:
        eui = input("Enter the letter :- ")
        if eui in dic:
            e += dic[eui] + "-"
        elif len(eui) == 0:
            e += "---"
        elif eui == "done":
            # code for writing in a file
            wd1 = input("Write data in a file? Y/N? :- ")
            if wd1 == "Y":
                fn1 = input("Enter file name with path:- ")
                f = open(fn1, "a")
                f.write(e)
                f.close()
                print("Data written in file")
            elif wd1 == "N":
                print("Okay,")
            else:
                print("I asked Y/N")
            break
        else:
            print("Unknown letter,No translation found")
# main code for decode
elif mui == "D" or mui == "Decode" or mui == "decode":
    while True:
        eui = input("Enter the letter :- ")
        if eui in endict:
            d += endict[eui]
        elif len(eui) == 0:
            d += " "
        elif eui == "done":
            # code for writing in a file
            wd = input("Write data in a file? Y/N? :- ")
            if wd == "Y":
                fn = input("Enter file name with path:- ")
                f = open(fn, "a")
                f.write(d)
                f.close()
                print("Data written in file")
            elif wd == "N":
                print("Okay,")
            else:
                print("I asked Y/N")
            break
        else:
            print("Unknown letter,No translation found")
else:
    print("Unknown command")
# Output
print(e)
print(d)
