CC = g++
LINKER = $(CC)

CXXFLAGS =  -std=c++20 -O2 -Wall
# CXXFLAGS += -g -DDEBUG

BIN := bin/main
SOURCES := $(wildcard *.cpp) $(wildcard src/*.cpp) $(wildcard src/*/*.cpp)
OBJECTS := $(patsubst %.cpp,%.o,$(SOURCES))
HEADERS := $(wildcard *.hpp) $(wildcard src/*.hpp) $(wildcard src/*/*.hpp) $(wildcard *.h) $(wildcard src/*.h) $(wildcard src/*/*.h)

all: virtualenv main test

main: $(BIN)


$(BIN): $(OBJECTS)
	$(LINKER) $^ $(LDFLAGS) -o $@

clean:
	rm -f $(OBJECTS) $(BIN) $(TEST_OBJECTS) $(TEST_BIN)
	rm -rf .venv

%.o: %.cpp $(HEADERS)
	$(CC) -c $(CFLAGS) $(CXXFLAGS) $< -o $@

test:
	. .venv/bin/activate && pytest -vv --html=report/report.html --self-contained-html; deactivate

virtualenv: .venv

.venv:
	python3 -m venv .venv
	. .venv/bin/activate && pip3 install --upgrade pip && pip3 install -r requirements.txt && deactivate

.PHONY: all main clean test virtualenv
