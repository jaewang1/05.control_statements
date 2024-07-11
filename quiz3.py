# for문과 range 함수를 사용해서
# 0~99까지 수를 한 라인에 하나씩 순차적으로 출력하는 프로그램 작성
result = []

for i in range(0, 100):
    result.append(i)
    print(i)
print(result)
