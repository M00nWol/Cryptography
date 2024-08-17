# 단순 치환 암호

import pyperclip, sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'
    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    myMode = 'decrypt' # Set to 'encrypt' or 'decrypt'

    if not keyIsValid(myKey):
        sys.exit('There is an error in the key or symbol set.')
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    
    print('Using key %s' % (myKey))
    print('The %sed message is: ' % (myMode))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('This message has been copied to the clipboard.')

def keyIsValid(key):
    keyList = list(key)
    letterList = list(LETTERS)
    keyList.sort()
    letterList.sort()

    return keyList == letterList

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated=''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # 복호화는 암호화와 같은 코드로 구현할 수 있다. 
        # 단지 key와 LETTERS를 교환해 문자열을 구축하면 된다.
        charsA, charsB = charsB, charsA
    
    # message의 각 심볼을 순회한다. 
    for symbol in message:
        if symbol.upper() in charsA:
            # 심볼을 암호화/복호화한다
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # 심볼이 LETTER 안에 없으면 그냥 덧붙인다. 
            translated += symbol
    
    return translated

def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

if __name__ == '__main__':
    main()
