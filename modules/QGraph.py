import networkx as nx

class QGraph:
	def __init__(self):
		self.graph = nx.Graph()
		
	def addNode(self, a):
		self.graph.add_node(a)
		
	def addEdge(self, a, b):		
		self.graph.add_edge(a, b)
		
	def controlZ(self, a, b):
		if self.graph.has_edge(a, b):
			self.graph.remove_edge(a,b)
		elif self.graph.has_node(a) and self.graph.has_node(b):
			self.graph.add_edge(a, b)
		else:
			print("Invalid Control Z operation. No such nodes [" + str(a) + "," + str(b) + "]")
		
	def localComplement(self, a):
		# get edges connected with a
		edges = []
		for e in self.graph.edges(a):
			edges.append(e)
		
		# remove a
		self.graph.remove_node(a)
		
		# complement graph
		self.graph = nx.complement(self.graph)
		
		# add a and all the edges
		self.graph.add_edges_from(edges)
		
	def z(self, a):
		if self.graph.has_node(a):
			self.graph.remove_node(a)
			
	def clear(self):
		self.graph.clear()
		
		
	def getState(self):
		state = ""		
		formatString = "{:>0" + str(self.graph.number_of_nodes()) + "b}"		
		nodeCount = 2**self.graph.number_of_nodes()
		
		for i in range(nodeCount):			
			isNegative = False
			
			subState = formatString.format(i)						
			
			for edge in self.graph.edges:
				if(subState[edge[0] - 1] == "1" and subState[edge[1] - 1] == "1"):
					isNegative = not isNegative
					
			if isNegative:
				state = state + " - |" + subState + ">"
			elif len(state) == 0:
				state = "|" + state + subState + ">"
			else:
				state = state + " + |" + subState + ">"
				
		print("State is 1/(sqrt(" + str(nodeCount) + ") (" +  state + ")")
		
		return state
						
