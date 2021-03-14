# ID успешной посылки 49359095
def zero(length, numbers):
    if length < 1 or length > 10 ** 6:
        return 'Incorrect length'
    s = 0
    z_index = None
    for i in range(length):
        if numbers[i] != 0 and z_index is None:
            numbers[i] = length
        elif numbers[i] != 0:
            s += 1
            numbers[i] = s
        elif numbers[i] == 0:
            s = 0
            z_index = i
    for i in range(length - 1, -1, -1):
        if i >= z_index:
            continue
        elif numbers[i] == 0:
            s = 0
        elif numbers[i] == length:
            s += 1
            numbers[i] = s
        elif numbers[i] != 0:
            numbers[i] = min(numbers[i], numbers[i + 1] + 1)

    return ' '.join(map(str, numbers))


def main():
    length = int(input())
    numbers = list(map(int, input().split()))
    print(zero(length, numbers))


if __name__ == "__main__":
    main()
