
arrayToIterate = "jjj.cnfgrova.pbz"
arrayOutput = ""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet2 = alphabet2
numOffset = 13
numb = 0

for ch in arrayToIterate.upper():
    numb = 0
    if ch != " ":
        for alphach in alphabet:
            
            if ch == alphach:
                arrayOutput += alphabet2[numOffset + numb:numOffset + numb + 1]
            numb += 1   
    else:
        arrayOutput += " "
        

print(arrayOutput)

