class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        import heapq
        min_heap = [1]
        for i in range(n):
        	res = heapq.heappop(min_heap)
        	while len(min_heap) > 0 and res == min_heap[0]:
        		res = heapq.heappop(min_heap)
        	heapq.heappush(min_heap, res * 2)
        	heapq.heappush(min_heap, res * 3)
        	heapq.heappush(min_heap, res * 5)
        return res
        
if __name__ == '__main__':
	n = 1690
	print(Solution().nthUglyNumber(n))
