from collections import deque

def bfs(graph,start_point,visited):

    queue=deque()
    queue.append(start_point)
    visited[start_point]=True
    
    while queue:
        source=queue.popleft()
        for g in graph[source]:
            if visited[g[0]]==0:
                visited[g[0]]=visited[source]+1 ## keypoint
                queue.append(g[0])
                
    return max(visited)


def solution(n, edge):
    
    answer = 0
    
    visited=[0]*(n+1) ## 편리하게하기위함 
    
    graph=[[] for _ in range(n+1)]
    for indiv in edge:
        ## 양방향
        graph[indiv[0]].append([indiv[1]])
        graph[indiv[1]].append([indiv[0]])

    #print(graph)
    max_iter=bfs(graph,1,visited) ## visited에는 방문 여부 뿐만아닌 edge 횟수까지 저장해야함
        
    ## list.count(해당노드 몇번출연?)
    return visited.count(max_iter)