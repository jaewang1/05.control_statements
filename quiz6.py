# 리스트 변수의 평균 값을 구하여라.
# my_list = [100, 200, 400, 800, 1000, 1300]
# data = []
# # 평균값을 구할 때는 for 반복문
# for my in my_list:
#     data.append(my)
# print(int(sum(data) / 6))


my_list = [100, 200, 400, 800, 1000, 1300]
result = 0
for i in my_list:
    result = result + i
avg = result / len(my_list)
print(int(avg))
