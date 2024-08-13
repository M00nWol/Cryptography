# 아핀 암호 해킹

import pyperclip, affineCipher, detectEnglish, cryptomath

SILENT_MODE = False

def main():
    myMessage = """"5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu"""

    hackedMessage = hackAffine(myMessage)

    if hackedMessage != None:
        # 화면에 평문이 표시된다. 
        # 사용자 편의를 위해 코드의 텍스트를 클립보드에 복사한다. 
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encryption')

def hackAffine(message):
    print('Hacking...')

    # 파이썬 프로그램을 중단하려면 Ctrl-C(윈도우)나 Ctrl-D(맥OS, 리눅스)를 아무 때나 누르면 된다.
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    # 가능한 모든 키를 무차별 대입법으로 넣어본다. 
    for key in range(len(affineCipher.SYMBOLS)**2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue
        
        decryptedText = affineCipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print('Tried Key %s... (%s)' % (key, decryptedText[:40]))

        if detectEnglish.isEnglish(decryptedText):
            # 복호화 키를 찾았는지 확인한다.
            print()
            print('Possible encryption hack:')
            print('Key: %s' % (key))
            print('Decrypted message: ' + decryptedText[:200])
            print()
            print('Enter D for done, or just press Enter to conticue hacking:')
            response = input('>')

            if response.strip().upper().startswith('D'):
                return decryptedText
    return None


# affineHacker.py를 모듈로 import한 것이 아니라면 main() 함수를 실행한다. 
if __name__ == '__main__':
    main()