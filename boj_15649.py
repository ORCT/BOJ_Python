def back_tracking

n,m = map(int, input().split())
for i in range(1,n+1):
    for j in range(1,m+1):
        print(f'{i} {j}')
#1부터 n 까지 중복없이 m 개를 고르는 수열
#for 안됨
#재귀로 구현하셈!
