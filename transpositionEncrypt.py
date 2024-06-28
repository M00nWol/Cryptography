# 전치 암호

import pyperclip

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    # ciphertext에 들어 있는 암호화된 문자열을
    # "파이프" 문자 |과 함께 출력하는데,
    # 암호화된 문자열의 끝에 공백이 있는 경우 이를 식별할 수 있다.
    print(ciphertext + '|')

    # ciphertext에 들어 있는 암호화된 문자열을 클립보드에 복사
    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    # ciphertext의 각 문자열은 격자상 하나의 열에서 온 것이다
    ciphertext = [''] * key

    # ciphertext의 각 열(column)을 순회한다.
    for column in range(key):
        currentIndex = column

        # currentInex가 message 길이를 넘을 때까지 순회를 계속한다.
        while currentIndex < len(message):
            # ciphertext 리스트 중 현재 column의 문자열 끝에 
            # message의 currentIndex의 문자를 넣는다
            ciphertext[column] += message[currentIndex]

            # currentIndex를 이동한다.
            currentIndex += key
        
    # ciphertext 리스트를 문자열 한 개로 변환하고 그것을 리턴한다. 
    return ''.join(ciphertext)


# transpositionEncrypt.py를 실행하면 (모듈로 import한 것이 아니면) main() 함수가 실행된다.
if __name__ == '__main__':
    main()