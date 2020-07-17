n = int(input())


########関数部分##############
def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n) + str(X%n).zfill(2)
    return str(X%n).zfill(2)
############################
 
 
#####関数をつかってみる．#####
x10 = n
x2 = Base_10_to_n(x10, 26)
print( x2,  x2[-2:])


l = list()
while x2:
    if 26 == int(x2[-2:]):
        l.append('z')
    
    else:
        l.append(chr(96 + int(x2[-2:])))
        
    x2 = x2[:-2]


ans = ''
for i in (reversed(l)):
    ans += i

    
print(ans)