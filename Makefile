.SUFFIXES: .c .cpp .o .x .h

SRCDIR:= src
OBJDIR = obj

NAME1 = bot
EXEC1 = $(NAME1).exe
OBJS1 = $(addprefix $(OBJDIR)/, $(NAME1).o)
SRC1 = $(addprefix $(SRCDIR)/, $(NAME1).cpp)

ifeq ($(OS),Windows_NT)
	NAME2 = http_windows
	OBJS2 = $(addprefix $(OBJDIR)/, $(NAME2).o)
	SRC2 = $(addprefix $(SRCDIR)/http_client/, $(NAME2).cpp)
	HEADS2 = $(addprefix $(SRCDIR)/http_client/, $(NAME2).hpp)

	LDLIBS = -lwinhttp
    RM = del /Q /S
else
	NAME2 = http_unix
	OBJS2 = $(addprefix $(OBJDIR)/, $(NAME2).o)
	SRC2 = $(addprefix $(SRCDIR)/http_client/, $(NAME2).cpp)
	HEADS2 = $(addprefix $(SRCDIR)/http_client/, $(NAME2).hpp)

	LDLIBS = -lcurl
    RM = rm -f
endif

CFLAGS = -std=c++11 -Wall
LFLAGS = -std=c++11 -Wall

CO = g++
LD = $(CO)

$(OBJS1): $(SRC1)
	$(CO) $(CFLAGS) -c $< -o $@
$(OBJS2): $(SRC2) $(HEADS2)
	$(CO) $(CFLAGS) -c $< -o $@

$(EXEC1): $(OBJS1) $(OBJS2)
		$(LD) -o $@ $(LFLAGS) $^ $(LDLIBS)

.PHONY: all
all: $(EXEC1)

.PHONY: run
run: $(EXEC1)
	./$(EXEC1)

.PHONY: clean
clean:
	$(RM) *.o *~ *.exe *.a *.x *.out
