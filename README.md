# CS260_P3
Programming assignment 3 for CS260

Assign yourself to 40 points worth of work. Don't take what has been claimed already. Make use of the folder structure that is in place. Update the readme with how to run your code. Python or C++ doesn't matter to me, just has to work.


Problem 1: The python file has all the program coded and the output of the file will give the answer of the best constants and explanation. Just type: python problem1.py  
The output will show the testing data. Our example data and tables of running it are shown as follows:
INSERTION
Key        Value      Running Time
Key1       3          1
Key2       4          1
Deletion - delete Key1
Key        Value      Running Time
Key1                  1
Key2       4          1



Problem 4: The supplement files for problem 4 are AliceInWonderland.txt and list_array.py. Make sure they have the same path as problem4.py does. First type:
            python problem4.py
The output will explain how the code works and at the end of explanation, it will ask you to input the file name you want to evaluate the tries size. After you entered the name, press return button, and the size of the file will be shown in the next line. 
For example, our text file is named "AliceInWonderland.txt". After you ran the program, you will see:
........ (explanation),
The size of the trie of Alice In Wonderland is: 
you can just input : AliceInWonderland.txt   and press enter
Then you will the tries size.

Problem 5: This uses the Dijkstra algorithm on problem number six of review 2 using the adjacency representation of the graph. The file, Dijkstra_AM.cpp, when run will print out the final vector D[], P[], and S[] which match that answers provided in the Review 2 solutions. This Fills all nodes not connected to one another/themselves with the INF infinity constant I defined as 100 in the adjacency matrix.

Problem 6: This uses the Dijkstra algorithm but in a more efficient manner, with a graph represented by an array of Nodes with adjacency lists and a partially ordered tree corresponding to the edge lengths. When run this program, Dijkstra_PoT, will print out the distances D[] for the minimal spanning graph. Note here, node 1 has distance 0 from itself unlike the previous implementation which has it at 100 (Infinity constant).

Problem 8: This implements a depth first search printing out a numbered list. Simply run the p8.py program within the python folder. This has a sample graph that is depicted in Figure 6.28 of the class textbook.

Problem 9: This implements the two recommended FFT algorithms and compares the output to the numpy implementation of fft, which is known to work. This program can be found in the python folder, simply run FFT.py. This output deviation between implemented algorithms and numpy's. Depending on the computer this may take a little bit to run. The results initially show deviation on the scale of 10^-28, which is small enough to be ignored.
