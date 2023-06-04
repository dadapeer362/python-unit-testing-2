# python-unit-testing-2

# To run the tests
1. pytest --> It is to execute the all test cases
2. pytest <file_name.py> --> It is to execute the particular file test cases
3. python -m -v pytest --> It is to execute the all test cases
4. pytest -m -v <marker_name> --> It is to execute the test cases based on the given marker
5. pytest -m -k <string_name> --> It is to execute the test cases which includes the given string
6. pytest -v --maxfail 2 --> It stops execution of test cases when ever it identifies two test cases failed
7. pytest --durations 3 --> It will give top 3 test cases which has taken longer time to execute
8. pytest -v -n <number> --> It is to execute the test cases parallely, number of parallel executions will happen based on the given number
9. pytest -v --junitxml="<file_name.xml>" --> It is to generate a test cases report in xml format
10. pytest -v --html="<file_name.html>" --> It is to generate a test cases report in html page

# Check list for writing test cases
1. Module name should start with test or ends with test
2. Function should start with test

# How to test the modules which does not start with test
1. Create file pytest.ini
2. Include below code of lines in pytest.ini
    here example taken as cg but it can be any name which wants to include for module names
    [pytest]
    python files = cg_*.py --> starts with cg
    python Classes = Cg
    python functions = *_cg --> ends with cg