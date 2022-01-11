# split, join

# split
a = 'My name is Joy'
print(a.split(sep=' ', maxsplit=-1))

# sep 가 delimiter, maxsplit 이 구분 횟수이다.
# sep = ' '이거나 None일 때, 띄어 쓰기 또는 Enter로 구분하며,
# maxsplit = -1일 때 무한이다
# sep = ' ' or None, maxsplit = -1이 default 값이다.
# default 값을 대입할 경우 생략 가능하다.

# split 값은 list로 반환된다.


# join

# split과 반대로 여러 string 자료를 하나의 string으로 합쳐 반환 해 준다.
# 합의 사이 문자열의 기준을 object로 .join(iterables) 메소드를 선언해 string을 반환한다.
# .join()의 반환값은 string

split_list = ['My', 'Name', 'is', 'Buds Pro']
join_dict = {'my name': 'Buds Pro', 'your name': 'Airpods Pro'}
# ' '.join(split_list)
# ' '.join(join_dict)

# Output
print(' '.join(split_list))
print(' '.join(join_dict))
