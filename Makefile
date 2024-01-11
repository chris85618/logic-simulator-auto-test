CC = g++
LINKER = $(CC)

REPORT := report/report.html

CXXFLAGS =  -std=c++20 -O2 -Wall
# CXXFLAGS += -g -DDEBUG

BIN := bin/main
SOURCES := $(wildcard *.cpp) $(wildcard src/*.cpp) $(wildcard src/*/*.cpp)
OBJECTS := $(patsubst %.cpp,%.o,$(SOURCES))
HEADERS := $(wildcard *.hpp) $(wildcard src/*.hpp) $(wildcard src/*/*.hpp) $(wildcard *.h) $(wildcard src/*.h) $(wildcard src/*/*.h)

VIRTUALENV_PATH = .venv

all: virtualenv main test

main: $(BIN)


$(BIN): $(OBJECTS)
	$(LINKER) $^ $(LDFLAGS) -o $@

cleanall: clean cleanvirtualenv
	rm -f $(REPORT)

clean:
	rm -f $(OBJECTS) $(BIN) $(TEST_OBJECTS) $(TEST_BIN)

cleanvirtualenv:
	rm -rf $(VIRTUALENV_PATH)

%.o: %.cpp $(HEADERS)
	$(CC) -c $(CFLAGS) $(CXXFLAGS) $< -o $@

test:
	. $(VIRTUALENV_PATH)/bin/activate && pytest -vv --html=$(REPORT) --self-contained-html; deactivate

virtualenv: $(VIRTUALENV_PATH)

$(VIRTUALENV_PATH):
	python3 -m venv $(VIRTUALENV_PATH)
	. $(VIRTUALENV_PATH)/bin/activate && pip3 install --upgrade pip && pip3 install -r requirements.txt && deactivate

.PHONY: all main clean test cleanall virtualenv cleanvirtualenv
