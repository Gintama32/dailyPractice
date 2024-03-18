x = 123
rev = 0
while x > 0:
    rem = x % 10
    x = x // 10
    rev = rev * 10 + rem
print(rev)
