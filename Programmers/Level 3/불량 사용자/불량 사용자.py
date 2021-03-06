from itertools import permutations


def isMatch(user_set, banned_set):
    for i in range(len(user_set)):
        if len(user_set[i]) != len(banned_set[i]):
            return False
        for j in range(len(user_set[i])):
            if banned_set[i][j] == '*':
                continue
            if user_set[i][j] != banned_set[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    ans = []

    for com_set in permutations(user_id, len(banned_id)):
        if isMatch(com_set, banned_id):
            com_set = set(com_set)

            if com_set not in ans:
                ans.append(com_set)

    return len(ans)