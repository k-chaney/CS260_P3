# Declaration of variables
CC = g++

BUILD=build/
OBJS=objects/
INCLUDES=includes/
SRC=src/

CC_FLAGS=-I$(INCLUDES)

make: DIRS D_TEST

DIRS:
	mkdir -p $(BUILD) $(OBJS)


D_TEST: DA.o DP.o
	$(CC) $(OBJS)DA.o -o $(BUILD)Dijkstra_AM
	$(CC) $(OBJS)DP.o -o $(BUILD)Dijkstra_PoT



# Obtain object files

DA.o:
	$(CC) -c $(CC_FLAGS) $(SRC)Dijkstra_AM.cpp -o $(OBJS)$@

DP.o:
	$(CC) -c $(CC_FLAGS) $(SRC)Dijkstra_PoT.cpp -o $(OBJS)$@

# To remove generated files
clean:
	rm -rf $(BUILD) $(OBJS)
