from collections import deque

def solution(maps):
    h = len(maps)
    w = len(maps[0])
    maps[h-1][w-1] = -1
    # 상하좌우
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # 그래프 초기화
    # graph = [[0] * w for i in range(h)]
    visited = [[0]*w for _ in range(h)]
    q = deque()
    answer = 1
    q.append((0, 0, answer))

    # 큐가 빌때까지 반복함
    while q:
        x, y, answer = q.popleft()
        # 현위치에서 네가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 공간을 벗어나느 경우 무시
            # print(f'nx : {nx}, ny : {ny}')
            if -1 < nx < h and -1 < ny < w:
                if maps[nx][ny] and visited[nx][ny] == 0:
                    maps[nx][ny] = answer + 1
                    visited[nx][ny] = 1
                    q.append((nx, ny, answer+1))

    return maps[h-1][w-1]