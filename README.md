# QGraph
A Python library for calculating quantum graph states

A graph state is a pure multipartite quantum state defined for a distributed quantum system.
A graph state can be defined in many ways.

1. Stabilizer based definition:

Let's define an operator


Then graph State G can be defined as 


2. Interaction definition

![alt text][interaction-def]

[interaction-def]: https://wikimedia.org/api/rest_v1/media/math/render/svg/ae08752ea63fa096226bdd346e3b420069fd452e "Operator" 

There are several important opeartions related to a graph state.
QGraph implements following.
1. Controlled-Z 
By applying a controlled-Z measurement between two qubits:
	If an edge already exists between the qubits, it is removed.
	Otherwise, an edge is added.
	
2. Z measurement
By measuring a qubit in Z basis removes that qubit(vertex) and all its edges.

3. Local complementation
Local complementation can be defined as an operator

It is also equivalent to 


How to use:
