from heapq import heappop,heappush

def solution(numbers):
    
    answer = [-1 for _ in range(len(numbers))]
    heap = [(numbers[0],0)]
    
    
    for i,n in enumerate(numbers[1:]):
        
        while heap and heap[0][0]<n:
            _,idx = heappop(heap)
            answer[idx] = n
            
        heappush(heap,(n,i+1))
        
    return answer