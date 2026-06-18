words = input("word: ")

for character in words:
    match character:
        case "A":
            ascii_code = 65
        case "B":
            ascii_code = 66
        case "C":
            ascii_code = 67
        case "D":
            ascii_code = 68
        case "E":
            ascii_code = 69
        case "F":
            ascii_code = 70
        case "G":
            ascii_code = 71
        case "H":
            ascii_code = 72
        case "I":
            ascii_code = 73
        case "J":
            ascii_code = 74
        case "K":
            ascii_code = 75
        case "L":
            ascii_code = 76
        case "M":
            ascii_code = 77
        case "N":
            ascii_code = 78
        case "O":
            ascii_code = 79
        case "P":
            ascii_code = 80
        case "Q":
            ascii_code = 81
        case "R":
            ascii_code = 82
        case "S":
            ascii_code = 83
        case "T":
            ascii_code = 84
        case "U":
            ascii_code = 85
        case "V":
            ascii_code = 86
        case "W":
            ascii_code = 87
        case "X":
            ascii_code = 88
        case "Y":
            ascii_code = 89
        case "Z":
            ascii_code = 90

        case "a":
            ascii_code = 97
        case "b":
            ascii_code = 98
        case "c":
            ascii_code = 99
        case "d":
            ascii_code = 100
        case "e":
            ascii_code = 101
        case "f":
            ascii_code = 102
        case "g":
            ascii_code = 103
        case "h":
            ascii_code = 104
        case "i":
            ascii_code = 105
        case "j":
            ascii_code = 106
        case "k":
            ascii_code = 107
        case "l":
            ascii_code = 108
        case "m":
            ascii_code = 109
        case "n":
            ascii_code = 110
        case "o":
            ascii_code = 111
        case "p":
            ascii_code = 112
        case "q":
            ascii_code = 113
        case "r":
            ascii_code = 114
        case "s":
            ascii_code = 115
        case "t":
            ascii_code = 116
        case "u":
            ascii_code = 117
        case "v":
            ascii_code = 118
        case "w":
            ascii_code = 119
        case "x":
            ascii_code = 120
        case "y":
            ascii_code = 121
        case "z":
            ascii_code = 122

        case " ":
            ascii_code = 32

    binary_number = bin(ascii_code)
    print(binary_number[2:],end=" ")
    
    
    
    
    
    
