def partition(s):
	ans = []
	def dfs(arr, str):
		if str:
			for i in range(1, len(str)+1):
				if str[:i] == str[:i][::-1]:
					dfs(arr+[str[:i]], str[i:])
				elif arr:
					ans.append(arr)
	dfs([],s)
	return ans