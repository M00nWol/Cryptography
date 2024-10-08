import math, pyperclip

def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plaintext = decryptMessage(myKey, myMessage)

    # 복호화된 메시지를 찍을 때 끝에 |(파이프 문자)를 같이 찍어서
    # 문자열 마지막에 공백이 있어도 알 수 있도록 한다.

    print(plaintext + '|')

    pyperclip.copy(plaintext)

def decryptMessage(key, message):
    # 전치 암호 복호화 함수는 문자열들의 리스트를 사용해 평문을 기록한 표의 "열"과 "행"을
    # 시뮬레이션한다. 먼저 몇 가지 값을 계산한다. 

    # 전치 그리드에서 사용할 columns의 길이
    numOfColumns = int(math.ceil(len(message) / float(key)))
    # 전치 그리드에서 사용할 rows의 길이
    numOfRows = key
    # 그리드의 마지막 "columns"에 칠할 박스의 숫자
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # 그리드의 열 한 개에 담긴 평문의 각 문자열
    plaintext = [''] * numOfColumns

    # 암호화된 message를 따라가며 그리드의 다음 글자를 가리키는 column과 row 변수

    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1 # 다음 칼럼을 지정한다. 

        # 더 이상 열이 없거나 검은 칠을 한 박스에 이르면
        # 첫 번째 열로 돌아가 다음 행 처리
        if(column == numOfColumns) or (column == numOfColumns-1 and row>= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)

# transpositionDecrypt.py를 모듈로 import하지 않고 실행했다면 main() 함수를 호출

if __name__ == '__main__':
    main()