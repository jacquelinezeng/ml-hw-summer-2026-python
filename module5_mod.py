class NumberList:
    def __init__(self):
        self.numbers=[]

    def initialize_data(self, n):
        self.numbers=[]
        for i in range(n):
            number=int(input(f'Enter number {i+1}: '))
            self.numbers.append(number)

    def search_number(self, x):
        for i in range(len(self.numbers)):
            if self.numbers[i]==x:
                return i+1

        return -1