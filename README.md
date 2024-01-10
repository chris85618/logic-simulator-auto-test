# logic-simulator-auto-test

## Introduction

* This program is to automatically test the homework for new comers to enter SELab/SDTLab.
* There are several test cases for the behavior and memory leak issues.
* Please **CHECK the TEST REPORTS MANUALLY** that the reason test failed might result from the output of their result not fully matching to the given question(specification).


## Get Started

### Setup Environments

* There are 2 ways to setup the environment.

#### With Docker

1. Reference [the offical guide](https://docs.docker.com/engine/install/) to install Docker in your system.

#### With Linux commands/WSL

1. Please install **C++ build environments**, **GNU make**, **Python3**, and **Virtual Environemnt for Python3** to execute these test cases.
    * For example, you can install `build-essential`, `make`, `python3`, and `python3-virtualenv` for Ubuntu.

### Execute Tests

#### With Docker

1. docker run -v <source-code-of-a-new-comer>:/source/src -v <report-directory>:/source/report --user ${UID}:${PID} -t --rm chris85618/logic-simulator-auto-test

#### With Linux commands/WSL

1. Sync this repository.
2. `cd logic-simulator-auto-test`
3. Place the source codes of a new comer into `src/`
4. Enter virtual environment: `source .venv/bin/activate`
5. Run `make`
6. Exit from the virtual environment: `deactivate`

### Check the test report

#### With Docker

1. Open `<report-directory>/report.html` with your browser for the test report.

#### With Linux commands/WSL

1. Open `<logic-simulator-auto-test>/report/report.html` with your browser for the test report.

## Limitation

1. The test report can't be viewed normally in mobiles.

## Build your own Docker Image

1. `docker build -t <image-name> .`
