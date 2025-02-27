import heapq

def return_n_smallest_chars(string):
    heap = []
    for char in string:
        heapq.heappush(heap, char)
        if len(heap) > 35:
            heapq.heappop(heap)
    sorted_heap = heapq.nsmallest(len(heap), heap)
    return sorted_heap[::-1]