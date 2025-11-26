#!/usr/bin/python3
for i in range(0, 100):
    ones = i%10
    tens = (i//10)%10
    if ones <= tens:
        continue
    if i == 89:
        print(f"{i:02}", end='')
    else:
        print(f"{i:02}", end=', ')
print()
