from collections import defaultdict

class TrieNode(object):
	def __init__(self):
		self.nodes = defaultdict(TrieNode)
		self.isword = False

class Trie(object):
	def __init__(self):
		self.root = TrieNode()
	def insert(word):
		curr = self.root
		for char in word:
			curr = curr.nodes[char]
		curr.isword = True
	def search(word):
		curr = self.root
		for char in word:
			if char not in curr.nodes:
				return False
			curr = curr.nodes[char]
		return curr.isword
	def startsWith(prefix):
		curr = self.root
		for char in prefix:
			if char not in curr.nodes:
				return False
			curr = curr.nodes[char]
		return True