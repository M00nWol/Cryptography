# 이 프로그램은 아핀 암호의 키 공간이 len(SYMBOLS) ^ 2 미만인 것을 검증한다.

import affineCipher, cryptomath

message = 'Make things as simple as possible, but not simpler.'
for keyA in range(2, 80):
    key = keyA * len(affineCipher.SYMBOLS) + 1

    if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) == 1:
        print(keyA, affineCipher.encryptMessage(key, message))