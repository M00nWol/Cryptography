# 뒤집기 암호

message = input('Enter message:')
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)