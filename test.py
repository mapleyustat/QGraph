from modules import QGraph
import networkx as nx

def main():
	print("Hello, QGraph!")

	qG = QGraph.QGraph()

	qG.addEdge(1,2)
	qG.addEdge(2,3)
	qG.addEdge(1,3)

	qG.getState()
	
	qG.z(3)
	
	qG.getState()
	
	print("Complete Graph K-10")
	
	qG.clear()
	k10 = nx.complete_graph(10)
	
	for edge in k10.edges:
		qG.addEdge(edge[0], edge[1])
		
	qG.getState()

if __name__ == "__main__":
	main()
