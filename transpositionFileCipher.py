# 전치 파일 암호 암호화/복호화

import time, os, sys ,transpositionEncrypt, transpositionDecrypt

def main():
    inputFilename = 'frankenstein.txt'
    # 주의! outputFilename으로 지정한 이름의 파일이 이미 존재하면
    # 프로그램이 그 파일을 덮어 쓸 것이다
    outputFilename = 'frankenstein.encrypted.txt'
    myKey = 10
    myMode = 'decrypt' # 'encrypt'나 'decrypt' 중에 하나를 설정한다. 

    # 입력 파일이 존재하지 않으면 프로그램을 조기에 종료시킨다. 
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' % (inputFilename))
        sys.exit()

    # 출력 파일이 이미 있으면 사용자에게 종료시킬지 선택의 기회를 준다.
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
        response = input('>')
        if not response.lower().startswith('c'):
            sys.exit
    
    # 입력 파일에서 message를 읽는다. 
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    # 암호화/복호화에 걸리는 시간을 측정한다. 
    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion Time: %s seconds' % (myMode.title(), totalTime))

    # 변환된 message를 출력 파일에 쓴다. 
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))


# transpositionFileCipher.py를 모둘이 아니라 직접 실행했다면 main() 함수를 호출한다. 
if __name__ == '__main__':
    main()