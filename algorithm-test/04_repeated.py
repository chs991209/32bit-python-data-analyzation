# 반복문

# range
# range(시작 값, 멈춤 값, 증가값(증가))
for a in range(0, 7, 2):
    print(a)


# enumerate
# Indexing
# enumerate(반복 대상 자료, Index 시작 값)

Enum = ['1', '2', '3', '4']

for index, value in enumerate(Enum, 2):
    print(index, value)

# While

# 증감식을 while 문 내부에 작성

# 초기화
i = 1
sum = 0

while i <= 100:
    sum += i
    i += 1

print(sum)

# while, break, continue
k = 1
sum1 = 0

while k <= 100:
    k += 1
    if (k % 2) != 0:
        continue
    sum1 += k

print(sum1)



