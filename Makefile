.SUFFIXES: .c .cpp .o .x .h

DIR = `basename $(CURDIR)`

NAME1 = bot

EXEC1  = $(NAME1).exe
OBJS1  = $(NAME1).o
#HEADS1 = 

CFLAGS = -std=c++11 -Wall
LFLAGS = -std=c++11 -Wall

LDLIBS = 

CO = g++
LD = $(CO)

%.o: %.cpp %.h
	$(CO) $(CFLAGS) -c $<

%.o: %.cpp
	$(CO) $(CFLAGS) -c $<

.PHONY: all
all: $(EXEC1)

$(EXEC1): $(OBJS1)
	$(LD) -o $@ $(LFLAGS) $^ $(LDLIBS)

#$(OBJS1): $(HEADS1)

.PHONY: run
run: $(EXEC1)
	./$(EXEC1)

.PHONY: clean
clean:                                                     
	del /Q *.o *~ *.exe *.a *.x *.out
