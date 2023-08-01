# 반복문

def fib_loop(n):
    result = [1, 1]

    for i in range(1, n):
        end1 = result[-1]                    # 리스트 뒤에서 접근
        end2 = result[len(result) - 2]       # 리스트 앞에서 접근할 때
        fib_num = end1 + end2

        result.append(fib_num)
        
    return result[-1]

fib_loop(6)

# 재귀

def fib_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib_rec(n-2) + fib_rec(n-1)

fib_rec(6)