.SUFFIXES: .c .cpp .o .x .h

SRCDIR:= src
OBJDIR = obj

NAME1 = bot
EXEC1 = $(NAME1).exe
OBJS1 = $(addprefix $(OBJDIR)/, $(NAME1).o)
SRC1 = $(addprefix $(SRCDIR)/, $(NAME1).cpp)
#HEADS1 = 

CFLAGS = -std=c++11 -Wall
LFLAGS = -std=c++11 -Wall
LDLIBS = 
CO = g++
LD = $(CO)

ifeq ($(OS),Windows_NT)
    RM = del /Q /S
else
    RM = rm -f
endif

$(OBJS1): $(SRC1) #$(HEADS1)
	$(CO) $(CFLAGS) -c $< -o $@
$(EXEC1): $(OBJS1)
	$(LD) -o $@ $(LFLAGS) $^ $(LDLIBS)

.PHONY: all
all: $(EXEC1)

.PHONY: run
run: $(EXEC1)
	./$(EXEC1)

.PHONY: clean
clean:
	$(RM) *.o *~ *.exe *.a *.x *.out
