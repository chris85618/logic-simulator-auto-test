import pytest
import subprocess

@pytest.mark.timeout(10)
def test_suite():
    result = subprocess.run(["./bin/main"], input=b"4\n", capture_output=True, shell=True, check=True)
    assert result.returncode == 0

    stdoutStrList = [line.strip() for line in result.stdout.splitlines() if len(line.strip()) > 0]
    assert [b'1. Load logic circuit file',
b'2. Simulation',
b'3. Display truth table',
b'4. Exit',
b'Command:Goodbye, thanks for using LS.'] == stdoutStrList


@pytest.mark.timeout(10)
def test_check_load():
    result = subprocess.run(["./bin/main"], input=b"1\ntests/test_data/selab01.lcf\n1\ntests/test_data/selab9999.lcf\n1\ntests/test_data/selab05.lcf\n3\n4\n", capture_output=True, shell=True, check=True)
    assert result.returncode == 0

    stdoutStrList = [line.strip() for line in result.stdout.splitlines() if len(line.strip()) > 0]
    assert [b"1. Load logic circuit file",
            b"2. Simulation",
            b"3. Display truth table",
            b"4. Exit",
            b"Command:Please key in a file path: Circuit: 3 input pins, 1 output pins and 3 gates",
            b"1. Load logic circuit file",
            b"2. Simulation",
            b"3. Display truth table",
            b"4. Exit",
            b"Command:Please key in a file path: File not found or file format error!!",
            b"1. Load logic circuit file",
            b"2. Simulation",
            b"3. Display truth table",
            b"4. Exit",
            b"Command:Please key in a file path: Circuit: 1 input pins, 1 output pins and 1 gates",
            b'1. Load logic circuit file',
            b'2. Simulation',
            b'3. Display truth table',
            b'4. Exit',
            b'Command:Truth table:',
            b'i | o',
            b'1 | 1',
            b'--+--',
            b'0 | 1',
            b'1 | 0',
            b"1. Load logic circuit file",
            b"2. Simulation",
            b"3. Display truth table",
            b"4. Exit",
            b"Command:Goodbye, thanks for using LS."] == stdoutStrList


@pytest.mark.timeout(10)
def test_check_simulate():
    result = subprocess.run(["./bin/main"], input=b"1\ntests/test_data/selab06.lcf\n2\n0\n1\n0\n1\n4\n", capture_output=True, shell=True, check=True)
    assert result.returncode == 0
    stdoutStrList = [line.strip() for line in result.stdout.splitlines() if len(line.strip()) > 0]
    assert stdoutStrList == [b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Please key in a file path: Circuit: 4 input pins, 2 output pins and 6 gates',
                             b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Please key in the value of input pin 1: Please key in the value of input pin 2: Please key in the value of input pin 3: Please key in the value of input pin 4: Simulation Result:',
                             b'i i i i | o o',
                             b'1 2 3 4 | 1 2',
                             b'--------+----',
                             b'0 1 0 1 | 0 1',
                             b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Goodbye, thanks for using LS.']


@pytest.mark.timeout(10)
def test_selab01():
    result = subprocess.run(["./bin/main"], input=b"1\ntests/test_data/selab01.lcf\n3\n4\n", capture_output=True, shell=True, check=True)
    assert result.returncode == 0
    stdoutStrList = [line.strip() for line in result.stdout.splitlines() if len(line.strip()) > 0]
    assert stdoutStrList == [b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Please key in a file path: Circuit: 3 input pins, 1 output pins and 3 gates',
                             b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Truth table:',
                             b'i i i | o',
                             b'1 2 3 | 1',
                             b'------+--',
                             b'0 0 0 | 0',
                             b'0 0 1 | 0',
                             b'0 1 0 | 0',
                             b'0 1 1 | 0',
                             b'1 0 0 | 1',
                             b'1 0 1 | 1',
                             b'1 1 0 | 0',
                             b'1 1 1 | 0',
                             b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Goodbye, thanks for using LS.']


@pytest.mark.timeout(10)
def test_selab02():
    result = subprocess.run(["./bin/main"], input=b"1\ntests/test_data/selab02.lcf\n3\n4\n", capture_output=True, shell=True, check=True)
    assert result.returncode == 0
    stdoutStrList = [line.strip() for line in result.stdout.splitlines() if len(line.strip()) > 0]
    assert stdoutStrList == [b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Please key in a file path: Circuit: 4 input pins, 3 output pins and 5 gates',
                             b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Truth table:',
                             b'i i i i | o o o',
                             b'1 2 3 4 | 1 2 3',
                             b'--------+------',
                             b'0 0 0 0 | 1 0 1',
                             b'0 0 0 1 | 1 0 0',
                             b'0 0 1 0 | 1 0 1',
                             b'0 0 1 1 | 1 0 0',
                             b'0 1 0 0 | 1 0 1',
                             b'0 1 0 1 | 1 0 0',
                             b'0 1 1 0 | 1 0 1',
                             b'0 1 1 1 | 1 0 0',
                             b'1 0 0 0 | 1 0 1',
                             b'1 0 0 1 | 1 0 0',
                             b'1 0 1 0 | 1 0 1',
                             b'1 0 1 1 | 1 0 0',
                             b'1 1 0 0 | 0 0 1',
                             b'1 1 0 1 | 0 0 0',
                             b'1 1 1 0 | 0 1 1',
                             b'1 1 1 1 | 0 1 0',
                             b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Goodbye, thanks for using LS.']


@pytest.mark.timeout(10)
def test_selab03():
    result = subprocess.run(["./bin/main"], input=b"1\ntests/test_data/selab03.lcf\n3\n4\n", capture_output=True, shell=True, check=True)
    assert result.returncode == 0
    stdoutStrList = [line.strip() for line in result.stdout.splitlines() if len(line.strip()) > 0]
    assert stdoutStrList == [b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Please key in a file path: Circuit: 2 input pins, 1 output pins and 1 gates',
                             b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Truth table:',
                             b'i i | o',
                             b'1 2 | 1',
                             b'----+--',
                             b'0 0 | 0',
                             b'0 1 | 0',
                             b'1 0 | 0',
                             b'1 1 | 1',
                             b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Goodbye, thanks for using LS.']


@pytest.mark.timeout(10)
def test_selab04():
    result = subprocess.run(["./bin/main"], input=b"1\ntests/test_data/selab04.lcf\n3\n4\n", capture_output=True, shell=True, check=True)
    assert result.returncode == 0
    stdoutStrList = [line.strip() for line in result.stdout.splitlines() if len(line.strip()) > 0]
    assert stdoutStrList == [b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Please key in a file path: Circuit: 2 input pins, 1 output pins and 1 gates',
                             b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Truth table:',
                             b'i i | o',
                             b'1 2 | 1',
                             b'----+--',
                             b'0 0 | 0',
                             b'0 1 | 1',
                             b'1 0 | 1',
                             b'1 1 | 1',
                             b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Goodbye, thanks for using LS.']


@pytest.mark.timeout(10)
def test_selab05():
    result = subprocess.run(["./bin/main"], input=b"1\ntests/test_data/selab05.lcf\n3\n4\n", capture_output=True, shell=True, check=True)
    assert result.returncode == 0
    stdoutStrList = [line.strip() for line in result.stdout.splitlines() if len(line.strip()) > 0]
    assert stdoutStrList == [b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Please key in a file path: Circuit: 1 input pins, 1 output pins and 1 gates',
                             b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Truth table:',
                             b'i | o',
                             b'1 | 1',
                             b'--+--',
                             b'0 | 1',
                             b'1 | 0',
                             b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Goodbye, thanks for using LS.']


@pytest.mark.timeout(10)
def test_selab06():
    result = subprocess.run(["./bin/main"], input=b"1\ntests/test_data/selab06.lcf\n3\n4\n", capture_output=True, shell=True, check=True)
    assert result.returncode == 0
    stdoutStrList = [line.strip() for line in result.stdout.splitlines() if len(line.strip()) > 0]
    assert stdoutStrList == [b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Please key in a file path: Circuit: 4 input pins, 2 output pins and 6 gates',
                             b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Truth table:',
                             b'i i i i | o o',
                             b'1 2 3 4 | 1 2',
                             b'--------+----',
                             b'0 0 0 0 | 1 0',
                             b'0 0 0 1 | 1 1',
                             b'0 0 1 0 | 1 0',
                             b'0 0 1 1 | 1 1',
                             b'0 1 0 0 | 0 0',
                             b'0 1 0 1 | 0 1',
                             b'0 1 1 0 | 0 0',
                             b'0 1 1 1 | 0 1',
                             b'1 0 0 0 | 0 0',
                             b'1 0 0 1 | 0 1',
                             b'1 0 1 0 | 0 0',
                             b'1 0 1 1 | 0 1',
                             b'1 1 0 0 | 0 0',
                             b'1 1 0 1 | 0 1',
                             b'1 1 1 0 | 0 0',
                             b'1 1 1 1 | 0 1',
                             b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Goodbye, thanks for using LS.']


@pytest.mark.timeout(10)
def test_selab07():
    result = subprocess.run(["./bin/main"], input=b"1\ntests/test_data/selab07.lcf\n3\n4\n", capture_output=True, shell=True, check=True)
    assert result.returncode == 0
    stdoutStrList = [line.strip() for line in result.stdout.splitlines() if len(line.strip()) > 0]
    assert stdoutStrList == [b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Please key in a file path: Circuit: 1 input pins, 1 output pins and 0 gates',
                             b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Truth table:',
                             b'i | o',
                             b'1 | 1',
                             b'--+--',
                             b'0 | 0',
                             b'1 | 1',
                             b'1. Load logic circuit file',
                             b'2. Simulation',
                             b'3. Display truth table',
                             b'4. Exit',
                             b'Command:Goodbye, thanks for using LS.']

@pytest.mark.timeout(10)
def test_no_any_memory_leak():
    result = subprocess.run(["valgrind --leak-check=full --show-leak-kinds=all --verbose ./bin/main"], input=b"1\ntests/test_data/selab01.lcf\n1\ntests/test_data/selab9999.lcf\n1\ntests/test_data/selab05.lcf\n3\n4\n", capture_output=True, shell=True)

    stderrStrList = [line.strip() for line in result.stderr.splitlines() if len(line.strip()) > 0]

    assert result.stderr.endswith(b"ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)\n")
    assert result.returncode == 0

@pytest.mark.timeout(10)
def test_no_any_memory_leak_error():
    result = subprocess.run(["valgrind --leak-check=full --show-leak-kinds=all --verbose ./bin/main"], input=b"1\ntests/test_data/selab01.lcf\n1\ntests/test_data/selab9999.lcf\n1\ntests/test_data/selab05.lcf\n3\n4\n", capture_output=True, shell=True)

    assert b"All heap blocks were freed -- no leaks are possible" in result.stderr
