# At first I solve this problem by minimum heap, but every time I get three new ugly number, I must judge whether it's duplicated in the heap. That's too complicated than it should be.
# After that I realized that the next minimum ugly number must be one in three(the u2, u3, u5 below).
# The time cost for the first method is about twice the second one.

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

    def nthUglyNumber2(self, n):
	    ugly = [1]
	    i2, i3, i5 = 0, 0, 0
	    u2, u3, u5 = 2, 3, 5
	    while n > 1:    
	        umin = min((u2, u3, u5))
	        ugly.append(umin)
	        if umin == u2:
	            i2 += 1
	            u2 = 2 * ugly[i2]
	        if umin == u3:
	            i3 += 1
	            u3 = 3 * ugly[i3]
	        if umin == u5:
	            i5 += 1
	            u5 = 5 * ugly[i5]
	        n -= 1
	    return ugly[-1]
        
if __name__ == '__main__':
	n = 1690
	print(Solution().nthUglyNumber(n))
	print(Solution().nthUglyNumber2(n))
