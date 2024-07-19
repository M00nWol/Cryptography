# 전치 암호 테스트

import random, sys, transpositionEncrypt, transpositionDecrypt

def main():
    random.seed(42) # 무작위 랜덤 함수의 초기화를 위한 시드값을 상수로 설정

    for i in range(20): # 20회 테스트한다

        # 테스트용 무작위 메시지를 생성
        # 이 메시지는 길이가 임의의 값이 될 것
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        # message 문자열을 뒤섞기 위해 리스트로 만듦
        message = list(message)
        random.shuffle(message)
        message = ''.join(message) # 리스트를 다시 문자열로 만든다

        print('Test #%s: "%s..."' % (i+1, message[:50]))

        # 각 message에 대해 가능한 모든 키 값을 확인한다
        for key in range(1, int(len(message)/2)):
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            # 원래 message와 복호화된 message가 다르면
            # 에러 메시지를 출력하고 프로그램을 탈출
            if message != decrypted:
                print('Mismatch with key %s and message %s.' % (key, message))
                print('Decrypted as: ' + decrypted)
                sys.exit()

    print('Transposition cipher test passed.')
 
# transpositionTest.py를 실행한 것이면 (모듈로 import한 것이 아니라) main() 함수를 호출한다
if __name__ == '__main__':
    main()
    