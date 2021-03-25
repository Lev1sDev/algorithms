# ID успешной посылки 49852259
from operator import add, floordiv, mul, sub


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        raise IndexError('pop from empty stack')


def main():
    seq = list(map(str, input().split()))
    OPERATOR = {
        '+': add,
        '-': sub,
        '/': floordiv,
        '*': mul
    }
    stack = Stack()
    for i in seq:
        if i not in OPERATOR:
            stack.push(int(i))
        else:
            a = stack.pop()
            b = stack.pop()
            stack.push(OPERATOR[i](b, a))
    print(stack.pop())


if __name__ == "__main__":
    main()
