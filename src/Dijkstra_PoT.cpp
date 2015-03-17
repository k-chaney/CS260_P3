// Dijkstra_PoT.cpp
// Description - This is the Dijkstra algorithm using a partially ordered
// tree as the representation of the graph. Main tests the algorigthm on the
// graph used for question 6 of the test 2 review.
//
// Alan Palmer
// 03/15/2015

// Imports
#include <stdio.h>
#include <iostream>

// Constants
const int MAX = 6;
const int INF = 100;

// Node Types
typedef int NODE;
typedef int POTNODE;

// List
typedef struct CELL *LIST;
struct CELL {
	NODE name;
	float label;
	LIST next;
};

// Graph
typedef struct DIRGRAPH GRAPH[MAX];
struct DIRGRAPH{
	float dist;
	LIST successors;
	POTNODE toPOT;
};

typedef NODE POT[MAX+1];


// Initialize the Graph and Tree
void initialize(GRAPH G, POT P, int *pLast){
	
	// Inialize all edges as INF
	for (int i = 0; i < MAX; ++i){
		G[i].dist = INF;
		G[i].toPOT = i+1;
		P[i+1] = i;
	}
	
	// first is 0 distance
	G[0].dist = 0;
	(*pLast) = MAX;
}

// Returns the priority of a node
float priority(POTNODE a, GRAPH G, POT P){

	// returns dist value
	return G[P[a]].dist;
}

// Swap to nodes on the tree
void swap(POTNODE a, POTNODE b, GRAPH G, POT P){

	NODE temp;
	// swap with temp
	temp = P[b];
	P[b] = P[a];
	P[a] = temp;
	G[P[a]].toPOT = a;
   G[P[b]].toPOT = b;
}

// Send Node a down tree
void sendDown(POTNODE a, GRAPH G, POT P, int last){

	// Define child
	POTNODE child;
	child = 2*a;

	// check if the next child has lower priority  
	if (child < last && priority(child+1, G, P) < priority(child, G, P)){
		child++;
	}

	// swap and call on next
	if (child <= last && priority(a, G, P) > priority(child, G, P)){
		swap(a, child, G, P);
		sendDown(child, G, P, last);
	}

}

// Send Node a up the tree
void sendUp(POTNODE a, GRAPH G, POT P){

	if (a > 1 && priority(a, G, P) < priority(a/2, G, P)){
		swap(a, a/2, G, P);
		sendUp(a/2, G, P);
	}
}

// Dijkstra Algorigthm
void Dijkstra(GRAPH G, POT P, int *pLast){
	
	// Variables 
	NODE u, v; // v is node we select to settle
	LIST ps; // list of successors to v

	// initialize graph and tree
	initialize(G, P, pLast);
	
	// main loop
	while ((*pLast) > 1) {
		v = P[1];
		swap(1, *pLast, G, P);
		--(*pLast);
		sendDown(1, G, P, *pLast);
		ps = G[v].successors;
		// update distances
		while (ps != NULL) {
			u = ps->name;
			if (G[u].dist > G[v].dist + ps->label){
				G[u].dist = G[v].dist + ps->label;
				sendUp(G[u].toPOT, G, P);
			}
			ps = ps->next;
		}
	}

	// Print distances
	std::cout << "Final Distances (D[]):" << std::endl;
	for(int i = 0; i < MAX; ++i){
		std::cout << G[i].dist << std::endl;
	}
}

int main() {
	
	// Problem 6, review 2

	// Define POT
	POT potNodes;

	// Define graph
	GRAPH graph;
	LIST succ1 = new CELL;
	
	//successors for source
	succ1->name = 1;
	succ1->label = 4;
	succ1->next = new CELL;

	LIST iter1 = succ1->next;
	iter1->name = 2;
	iter1->label = 1;
	iter1->next = new CELL;

	iter1 = iter1->next;
	iter1->name = 3;
	iter1->label = 5;
	iter1->next = new CELL;

	iter1 = iter1->next;
	iter1->name = 4;
	iter1->label = 8;
	iter1->next = new CELL;

	iter1 = iter1->next;
	iter1->name = 5;
	iter1->label = 10;
	iter1->next = NULL;

	// Add list to node 1
	graph[0].successors = succ1;

	// node 2 
	graph[1].successors = NULL; // no paths away
	
	// node 3 successors
	LIST succ3 = new CELL;

	succ3->name = 1;
	succ3->label = 2;
	succ3->next = NULL;

	graph[2].successors = succ3;

	// node 4
	LIST succ4 = new CELL;

	succ4->name = 4;
	succ4->label = 2;
	succ4->next = NULL;

	graph[3].successors = succ4;

	// node 5
	LIST succ5 = new CELL;

	succ5->name = 5;
	succ5->label = 1;
	succ5->next = NULL;

	graph[4].successors = succ5;

	// node 6
	graph[5].successors = NULL; //node 6 is end/no successors


	// Define Last
	int last = 6;

	// Use Dijkstra algorithm
	Dijkstra(graph, potNodes, &last);

}
