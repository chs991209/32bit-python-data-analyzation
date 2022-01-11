# Python 자료형
# int, complex, float, bool, ..


# 반복 자료형 Iterables

# List, Tuple, Dictionary
# Iterable >> 값/ 원소를 하나씩 꺼내어 처리할 수 있음

# List

# 가장 빈번하게 사용됨

# list(['a', 'b', 'c'])로 대입 값을 처리할 수 있음

a = ['a', 'b']
print(a)

# 원소로 다른 Iterables를 포함할 수 있다.

b = ['a', 'b', 'c']
c = ['a', 'b', {'c': 'd'}]

# reverse 함수
print(a.reverse())

# index 접근
# index 접근을 다중으로 할 수 있다.
# list 내의 list의 index 접근, list 내의 dict의 key 값을 통해 value에 접근


# list 간의 연산
# 합집합의 개념

add_list = a + b
print(add_list)

# 교집합 (set.intersection())
# 1차원 배열일 때만 가능하다.

common_list = list(set(a).intersection(b))
print(common_list)
