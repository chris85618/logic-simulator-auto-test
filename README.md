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

1. Please install **C++ build environments**, **GNU make**, **Python3**, **Virtual Environemnt for Python3**, and `Valgrind` to execute these test cases.
    * Take Ubuntu for an example, you can use `sudo apt update; sudo apt install build-essential make python3 python3-virtualenv valgrind` to install those packages.

### Execute Tests

#### With Docker

1. docker run -v <source-code-of-a-new-comer>:/source/src -v <report-directory>:/source/report --user ${UID}:${PID} -t --rm chris85618/logic-simulator-auto-test

#### With Linux commands/WSL

1. Sync this repository.
2. `cd logic-simulator-auto-test`
3. Place the source codes of a new comer into `src/`
4. Run `make`

### Check the test report

#### With Docker

1. Open `<report-directory>/report.html` with your browser for the test report.

#### With Linux commands/WSL

1. Open `<logic-simulator-auto-test>/report/report.html` with your browser for the test report.

## Limitation

1. The test report can't be viewed normally in mobiles.

## Build your own Docker Image

1. `docker build -t <image-name> .`
