class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        rounds = []
        for op in ops:
        	if op == 'C':
        		rounds.pop()
        	elif op == 'D':
        		rounds.append(2 * rounds[-1])
        	elif op == '+':
        		rounds.append(rounds[-1] + rounds[-2])
        	else:
        		rounds.append(int(op))

        return sum(rounds)

if __name__ == '__main__':
	ops = ["5","-2","4","C","D","9","+","+"]
	print(Solution().calPoints(ops))