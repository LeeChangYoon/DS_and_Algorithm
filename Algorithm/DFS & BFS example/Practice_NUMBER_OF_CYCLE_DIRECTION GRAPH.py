def dfs(_graph, _node):
    global visit, answer

    visit.append(_node)
    if _node not in _graph:
        return

    next_node = _graph[_node][:]
    for n in next_node:
        if n == visit[0]:
            answer += 1
            visit.append(n)
            continue

        if n in visit:
            visit.append(n)
            continue

        dfs(_graph, n)


visit = []
answer = 0

if __name__ == "__main__":
    f_input = open("input4.txt", 'r')
    f_output = open("output.txt", 'w')
    T = int(f_input.readline())

    while T > 0:
        N = int(f_input.readline().strip())
        graph = {}

        for idx in range(N):
            temp = list(map(int, f_input.readline().strip().split()))

            if 1 in temp:
                graph[idx] = []

            for i in range(len(temp)):
                if temp[i] == 1:
                    graph[idx].append(i)

        result = 0
        for node in list(graph.keys()):
            answer = 0
            visit = []
            dfs(graph, node)

            if answer > result:
                result = answer

        f_output.write(str(result) + "\n")
        T -= 1

    f_input.close()
    f_output.close()
