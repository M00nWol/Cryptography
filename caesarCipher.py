# 카이사르 암호화

import pyperclip

# 암호화/복호화할 문자열
message = 'This is my secret message.'

# 암호화/복호화 키
key = 13

# 암호화/복호화 모드 설정
# 'encrypt' 또는 'decrypt'를 써야함
mode = 'encrypt'

# 암호화 대상이 되는 모든 글자
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# message를 암호화/복호화해 저장할 변수
translated = ''

for symbol in message:
    # 주의 : SYMBOLS 문자열에 있는 문자만 암호화/복호화할 수 있다.
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # 암호화 / 복호화 수행
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # 필요하다면 한 바퀴 돌아서 처리한다.
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]

    else:
        # 암호화/복호화하지 않은 문자를 더한다
        translated = translated + symbol

# translated 문자열을 출력한다. 
print(translated)
pyperclip.copy(translated)


