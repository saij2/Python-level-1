words = (input("Enter the word: "))

match words:
    case "sad": 
        print("happy")
    case "up":
        print("down")
    case "tall":
        print("short")
    case "big":
        print("small")
    case "black":
        print("white")
    case "good":
        print("bad")
    case "light":
        print("dark")
    case "fun":
        print("boring")
    case "tired":
        print("energetic")
    case "cold":
        print("hot")
    case _ :
        print("Invalid word")

