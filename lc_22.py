def generateParenthesis(n):
	ans = []
	left, right = 0, 0
	cur =''
	def backtrack(ans, cur, left, right, n):
		if len(cur) == 2*n:
			ans.append(cur)
		if left < n:
			backtrack(ans, cur+'(', left +1, right, n)
		if right < left:
			backtrack(ans, cur+')', left, right+1, n)
		backtrack(ans, cur, left, right, n)
	return ans

