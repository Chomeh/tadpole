#tadpole

A testing tool for computer networks

''mytests.yaml''
    - !!python/object:tests.DummyTests.DummyPassTest {name: A dummy test that will pass}
    - !!python/object:tests.DummyTests.DummyFailTest {name: A dummy test that will fail}
    - !!python/object:tests.DummyTests.DummyErrorTest {name: A dummy test that will raise an exception}

python tadpole.py -f mytests.yaml

Output:
    A dummy test that will pass ... passed
    A dummy test that will fail ... failed
    A dummy test that will raise an exception ... error
    total passed 1/3

## Dependencies
* [Python 3](https://www.python.org/download/releases/3.0/)
* [pyyaml](http://pyyaml.org/)