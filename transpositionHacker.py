# 전치 암호 해킹

import pyperclip, detectEnglish, transpositionDecrypt

def main():
    myMessage = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr."""

    hackedMessage = hackTransposition(myMessage)

    if hackedMessage == None:
        print('Failed to hack encryption.')
    else:
        print('Copying hacked message to clipboard: ')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)

def hackTransposition(message):
    print('Hacking...')

    # 파이썬 프로그램은 다음 키를 누르면 아무 때라도 멈춘다.
    # Ctrl-C (윈도우). Ctrl-D (맥OS, Linux):
    print('(Press Ctrl-C (on Windows) or Ctrl-D (on 맥OS and Linux) to quit at any time.)')

    # 가능한 모든 키를 무차별 대입하는 순환문
    for key in range(1, len(message)):
        print('Trying key #%s...' % (key))

        decryptedText = transpositionDecrypt.decryptMessage(key, message)

        if detectEnglish.isEnglish(decryptedText):
            # 복호화가 잘 됐는지 사용자에게 질의
            print()
            print('Possible encrypting hack:')
            print('Key %s: %s' % (key, decryptedText[:100]))
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('>')

            if response.strip().upper().startswith('D'):
                return decryptedText
        
    return None

if __name__ == '__main__' :
    main()