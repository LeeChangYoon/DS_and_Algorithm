from collections import deque

str_list = None

def check():
    global str_list
    stack = []

    for _str in str_list:
        if _str in ('[', '(', '{'): stack.append(_str)
        else:
            if not stack: return False
            x = stack.pop()
            if _str == ']' and x != '[': return False
            elif _str == ')' and x != '(': return False
            elif _str == '}' and x != '{': return False

    if stack: return False
    return True

def solution(s):
    global str_list
    answer = 0
    for i in range(len(s)):
        str_list = deque(s)
        str_list.rotate(-i)
        if check(): answer += 1

    return answer