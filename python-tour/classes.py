class FirstClass:
    commonValue = 10

    def __init__(self):
        self.myValue = 100

    def myFunc(self, arg1, arg2):
        return self.myValue * arg1 * arg2


firstInstance = FirstClass()
result = firstInstance.myFunc(1, 2)
print(result)

secondInstance = FirstClass()
print()
