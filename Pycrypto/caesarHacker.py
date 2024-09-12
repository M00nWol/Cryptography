# 카이사르 암호 해킹

message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# 가능한 모든 키를 순회한다. 
for key in range(len(SYMBOLS)):
    # translated에 공백 문자열을 넣어서
    # 이전 순회의 translated 값을 비우는 것이 중요하다
    translated = ''

    # 프로그램의 남은 부분은 카이사르 프로그램과 거의 같다
    
    # message 안에 있는 각 심볼을 순회한다
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # 경계선 다루기
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            # 복호화된 심볼을 더한다
            translated = translated + SYMBOLS[translatedIndex]

        else:
            # 암호화/복호화 없이 심볼을 더한다
            translated = translated + symbol
        
    # 가능한 복호화를 모두 출력한다 
    print('Key #%s: %s' % (key, translated))