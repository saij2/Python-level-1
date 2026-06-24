morse = input('Morse Code: ')
print('Text: ', end=' ')

for code in morse.split(' '):
    match code:
        case '.-':
            print('a', end='')
        case '-...':
            print('b', end='')
        case '-.-.':
            print('c', end='')
        case '-..':
            print('d', end='')
        case '.':
            print('e', end='')
        case '..-.':
            print('f', end='')
        case '--.':
            print('g', end='')
        case '....':
            print('h', end='')
        case '..':
            print('i', end='')
        case '.---':
            print('j', end='')
        case '-.-':
            print('k', end='')
        case '.-..':
            print('l', end='')
        case '--':
            print('m', end='')
        case '-.':
            print('n', end='')
        case '---':
            print('o', end='')
        case '.--.':
            print('p', end='')
        case '--.-':
            print('q', end='')
        case '.-.':
            print('r', end='')
        case '...':
            print('s', end='')
        case '-':
            print('t', end='')
        case '..-':
            print('u', end='')
        case '...-':
            print('v', end='')
        case '.--':
            print('w', end='')
        case '-..-':
            print('x', end='')
        case '-.--':
            print('y', end='')
        case '--..':
            print('z', end='')
        case '-----':
            print('0', end='')
        case '.----':
            print('1', end='')
        case '..---':
            print('2', end=' ')
        case '...--':
            print('3', end='')
        case '....-':
            print('4', end='')
        case '.....':
            print('5', end=' ')
        case '-....':
            print('6', end='')
        case '--...':
            print('7', end='')
        case '---..':
            print('8', end=' ')
        case '----.':
            print('9', end='')
        case '/':
            print(' ', end=' ')
