CC = g++
LINKER = $(CC)

CXXFLAGS =  -std=c++20 -O2 -Wall
# CXXFLAGS += -g -DDEBUG

BIN := bin/main
SOURCES := $(wildcard *.cpp) $(wildcard src/*.cpp) $(wildcard src/*/*.cpp)
OBJECTS := $(patsubst %.cpp,%.o,$(SOURCES))
HEADERS := $(wildcard *.hpp) $(wildcard src/*.hpp) $(wildcard src/*/*.hpp) $(wildcard *.h) $(wildcard src/*.h) $(wildcard src/*/*.h)

all: main test

main: $(BIN)


$(BIN): $(OBJECTS)
	$(LINKER) $^ $(LDFLAGS) -o $@

clean:
	rm -f $(OBJECTS) $(BIN) $(TEST_OBJECTS) $(TEST_BIN)

%.o: %.cpp $(HEADERS)
	$(CC) -c $(CFLAGS) $(CXXFLAGS) $< -o $@

test:
	pytest -vv --html=report/report.html --self-contained-html

.PHONY: all main clean test
