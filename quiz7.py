# while문을 사용하여 1부터 45 사이의 랜덤한 수 6개 생성
# import random
# result = []
# # 이를 result 리스트 변수에 추가하는 코드 작성
# while len(result) < 6 :
#     data = random.randint(1, 45)
#     result.append(data)
#     print(data)


import random
result = []
i = 0
while i < 6 :
    i = i + 1
    result.append(random.randint(1, 45))
print(result)