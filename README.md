# QGraph
A Python library for calculating quantum graph states

A graph state is a pure multipartite quantum state defined for a distributed quantum system.
A graph state ![alt text][graph-state] can be defined in many ways.

[graph-state]:https://wikimedia.org/api/rest_v1/media/math/render/svg/400c00a32208beba543bbd67fdb9d01edcfd1918

1. Stabilizer based definition:

Let's define an operator
![alt text][stabilizer]
[stabilizer]:https://wikimedia.org/api/rest_v1/media/math/render/svg/17d5b8a474504396d2b54da0790e15bf9f6f95f7

where ![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/081d5c8414c5ff43d1f73fb79f98fc35af073ed0) are the Pauli matrices and N(v) is the set of vertices adjacent to v.
These ![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/92feed1a3e76a5a2bf8233f7376f6ddb932807f3) form a complete set of commuting observables (CSCO). Then we can define graph state ![alt text][graph-state] as the eigen state ![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/565ab2a736812d2720cd19246e95133aae9d217b)



2. Interaction definition

![alt text][interaction-def]

[interaction-def]: https://wikimedia.org/api/rest_v1/media/math/render/svg/ae08752ea63fa096226bdd346e3b420069fd452e

Here, ![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/a0047d653fc3fdb5a9f3831541747312e4841fd7) is the controlled-Z operation betweeen a and b. 

There are several important opeartions related to a graph state.
QGraph implements following.
1. Controlled-Z
	By applying a controlled-Z measurement between two qubits:
		If an edge already exists between the qubits, it is removed.
		Otherwise, an edge is added.
	
2. Z measurement
	By measuring a qubit in Z basis removes that qubit(vertex) and all its edges.

3. Local complementation
	Appplying opeartor for local complementation to a qubit/node a is equivalent to calculating the graph state where, we remove all the existing edges between the neighbours of a and add missing edges. 



How to use:
