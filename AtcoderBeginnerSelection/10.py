s=input()

s=s.replace('dreamer', '')
s=s.replace('dream', '')
s=s.replace('eraser', '')
s=s.replace('erase', '')

if s=='':
    print('YES')
else:
    print('NO')