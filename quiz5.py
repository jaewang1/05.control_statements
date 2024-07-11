# while문을 사용하여 1부터 100까지 수에 존재하는 모든 홀수의 합을 구하시오.
i = 0
data = 0
while i < 100:
    i = i + 1
    if i % 2 == 1:
        data = data + i
print(data)

# i = 0
# data = []
# while i < 100:
#     i = i + 1
#     if i % 2 == 1:
#         data.append(i)
# print(sum(data))






#
# i = 0
# while i < 1000:
#         i = i + 1
#         # if i == 500:
#         #     break
#         print("대기번호:", i, "번 입니다.")
# else:
#     print("대기번호가 1000번 초과입니다.")
