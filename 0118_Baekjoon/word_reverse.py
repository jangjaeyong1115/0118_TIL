import sys
input = sys.stdin.readline

Test_case = int(input()) # 테스트 케이스
for i in range(Test_case):
    sentence = list(input().rstrip().split())
    for word in sentence:
        print(word[::-1], end=" ")
    print()