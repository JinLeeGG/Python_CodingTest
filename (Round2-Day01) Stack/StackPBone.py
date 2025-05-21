
def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if not stack:
                return False
            else:
                stack.pop()

    if not stack:
        return True
    else:
        return False

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
print(solution("(())))"))


def solution2(s):
    for i in range(len(s) - 1):
        j = 0
        if (s[i] == "(") and (s[i+1] == ")"):
            pass
        else:
            j += 1
            
    if j == 0:
        return True
    else:
        return False
    


# print(solution2("()()"))
# print(solution2("(())()"))
# print(solution2(")()("))
# print(solution2("(()("))
            

        

        