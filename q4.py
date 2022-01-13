def solution(arr):
    lcm = 1
    for i in arr:
        lcm *= i
    answer = lcm + 1
    for i in range(max(arr), lcm+1):
        for j in arr:
            if i % j != 0:
                break
            else:
                if j == arr[-1]:
                    answer = i
                    break
        if answer < lcm:
            break
    return answer

arr = [None]*15
arr = [3,5,7,9]
answer = solution(arr)
print(answer)
