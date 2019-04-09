#ex 1.6.2 stack

class ExtendedStack(list):
    def sum(self):
        # операция сложения
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 + top2)
        return self 

    def sub(self):
        # операция вычитания
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 - top2)
        return self

    def mul(self):
        # операция умножения
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 * top2)
        return self

    def div(self):
        # операция целочисленного деления
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 // top2)
        return self