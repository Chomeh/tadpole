from tests.Test import Test


class DummyPassTest(Test):
    def __init__(self, name):
        super(DummyPassTest, self).__init__(name)

    @staticmethod
    def run():
        return True


class DummyFailTest(Test):
    def __init__(self, name):
        super(DummyFailTest, self).__init__(name)

    @staticmethod
    def run():
        return False


class DummyErrorTest(Test):
    def __init__(self, name):
        super(DummyErrorTest, self).__init__(name)

    @staticmethod
    def run():
        raise Exception("A dummy exception")