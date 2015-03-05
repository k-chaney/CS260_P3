# Declaration of variables
CC = g++

BUILD=build/
OBJS=objects/
INCLUDES=includes/
SRC=src/

CC_FLAGS=-I$(INCLUDES)

make: LLP_TEST

DIRS:
	mkdir -p $(BUILD) $(OBJS)

# Main tests
LLP_TEST: LLP.o LLP_TEST.o
	$(CC) $(OBJS)LLP.o $(OBJS)$@.o -o $(BUILD)$@



# Obtain object files

LLP.o:
	$(CC) -c $(CC_FLAGS) $(SRC)LL_Pointer.cpp -o $(OBJS)$@

LLP_TEST.o:
	$(CC) -c $(CC_FLAGS) $(SRC)LLP_Test.cpp -o $(OBJS)$@




# To remove generated files
clean:
	rm -rf $(BUILD) $(OBJS)
