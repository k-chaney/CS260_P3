# Declaration of variables
CC = g++

BUILD=build/
OBJS=objects/
INCLUDES=includes/
SRC=src/

CC_FLAGS=-I$(INCLUDES)

make: Dirs Dijkstra_Test

DIRS:
	mkdir -p $(BUILD) $(OBJS)

Dijkstra_Test:
	$(CC) $(SRC)Dijkstra_AM.cpp -o $(OBJS)$@
	$(CC) $(SRC)Dijkstra_PoT.cpp -o $(OBJS)$@
	$(OBJS)Dijkstra_AM
	$(OBJS)Dijkstra_PoT

# To remove generated files
clean:
	rm -rf $(BUILD) $(OBJS)
