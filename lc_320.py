def generateAbbreviations(word):
	result = []
	def dfs(pos, cur, count):
		if len(word) == pos:
			result.append(cur + str(count) if count > 0 else cur)
		else:
			dfs(pos+1, cur, count +1)
			dfs(pos +1, cur+(str(count) if count> 0 else '') + word[pos], 0)
	dfs(0, '', 0)
	return result