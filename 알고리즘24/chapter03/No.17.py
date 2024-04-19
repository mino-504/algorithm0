def nearest_neighbor(graph, start):
    path = [start]  # 시작 도시를 방문한 경로
    current_city = start  # 현재 위치를 시작 도시로 초기화
    
    while len(path) < len(graph):  # 모든 도시를 방문할 때까지 반복
        nearest_city = None  #nearest_city라는 변수를 선언해주고 none값으로 체운다
        min_distance = float('inf')  # 무한대로 초기화
        
        # 현재 도시와 연결된 도시들을 탐색하여 가장 가까운 도시 선택
        for neighbor in graph[current_city]:
            if neighbor not in path:   #연결된 지역이 중복이 아니라면
                distance = graph[current_city][neighbor]
                if distance < min_distance:
                    min_distance = distance
                    nearest_city = neighbor
        
        # 가장 가까운 도시를 방문한 경로에 추가하고 현재 도시를 업데이트
        path.append(nearest_city)
        current_city = nearest_city
    
    # 마지막으로 시작 도시로 돌아오는 경로 추가
    path.append(start)
    return path

# 간단한 그래프를 만들어 테스트
# 각 도시 간의 거리를 딕셔너리로 표현
graph = {
    'A': {'B': 2, 'C': 3, 'D': 4},
    'B': {'A': 2, 'C': 4, 'D': 2},
    'C': {'A': 7, 'B': 4, 'D': 5},
    'D': {'A': 4, 'B': 2, 'C': 3}
}

start_city = 'B'  # 시작 도시 선택
shortest_path = nearest_neighbor(graph, start_city)
print("최단 경로:", shortest_path)
