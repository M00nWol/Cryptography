# 영어 감지 모듈

# 이 코드를 사용하기 위해서는 아래 두 줄과 dictionary.txt가 있어야 함
# import detectEnglish
# detectEnglish.isEnglish(someString)

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()

    if possibleWords == []:
        return 0.0 # 단어가 없으면 0.0을 리턴한다. 

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    
    return float(matches) / len(possibleWords)


def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

def isEnglish(message, wordPercentage=20, letterPercentage=85):
    # 기본값으로 사전 파일에서 20% 단어가 존재하고, 
    # message의 문자가 85%가 글자나 공백이어야 한다. 
    # (특수문자나 숫자가 아니다)
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLetterPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLetterPercentage >= letterPercentage
    return wordsMatch and lettersMatch