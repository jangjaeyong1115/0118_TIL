test_case = int(input()) # 테스트 케이스

for i in range(test_case):
    repeat, char = input().split()
    for j in range(len(char)):
        print("{}".format(char[j]*int(repeat)),end= " ")

    print("")