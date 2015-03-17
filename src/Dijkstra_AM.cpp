// Dijkstra_AM.cpp
// Description - This is the Dijkstra algorithm using an adjecency matrix as
// the representation of the graph. Main tests the algorigthm on the
// graph used for question 6 of the test 2 review.
//
// Alan Palmer
// 03/15/2015

// Imports
#include <stdio.h>
#include <iostream>
#include <ostream>

// Constants
const int INF = 100;




int main() {
	
	// Problem 6, review 2
	// Define graph
	int n = 7; // 0 - 6
	int G[n][n];

	// fill G
	for(int i = 0; i < n; ++i){
		for (int j = 0; j < n; ++j){
			G[i][j] = INF;
		}
	}

	G[1][2] = 4;
	G[1][3] = 1;
	G[1][4] = 5;
	G[1][5] = 8;
	G[1][6] = 10;
	G[3][2] = 2;
	G[4][5] = 2;
	G[5][6] = 1;

	

	// Use Dijkstra algorithm
// Dijkstra Algorigthm Using Adjacency matrix
	
	// Variables 
	int u, w, v; // v is node we select to settl
	int S[n], D[n], P[n], temp[n];
	
	// initialize graph and tree
	for(int i = 1; i < n; ++i){
		D[i] = G[1][i];
		P[i] = 1;
	}
	
	S[1] = 1;

	// main loop
	for(u = 1; u < n-1; ++u){
		w = INF;
		//make temp of D
		for(int b = 1; b < n; ++b){
			temp[b] = D[b];
		}

		// make sure S are not reepeated
		for(int k = 1; k <= u; ++k){
			int t = S[k];
			temp[t] = INF;
		}
		// get minimum w
		for(int m = 2; m < n; ++m){
			if(temp[m] < w){
				w = m;
			}
		}
		// add w to S
		S[u+1] = w;
		// update distances
		for(v = 1; v < n; ++v){
			if(D[v] > D[w]+G[w][v]){
				D[v] = D[w] + G[w][v];
				P[v] = w;
			}
		}
	}

	// Print D, S, and P
	std::cout << "D vector: " << std::endl;
	for(int i = 1; i < n; ++i){
		std::cout << D[i] << std::endl;
	}

	std::cout << "P vector: " << std::endl;
	for(int i = 1; i < n; ++i){
		std::cout << P[i] << std::endl;
	}

	std::cout << "S vector: " << std::endl;
	for(int i = 1; i < n; ++i){
		std::cout << S[i] << std::endl;
	}


}
