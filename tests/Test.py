class Test(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    # Runs the test.
    # Returns True if the test passed, False if the test failed
    # or raises an exception if the test could not be performed
    def run(self):
        raise NotImplementedError("Please Implement this method")

