class BaseTest:
    @staticmethod
    def first_method():
        a = 1
        b = 2
        if (a + b) == 4:
            print('False')
        elif (a + b) == 3:
            print('True')

    first_method()
