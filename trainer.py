# ID успешной посылки 49359028
def trainer(fingers, symbols) -> int:
    if fingers > 5 or fingers < 1:
        return 'Incorrect count fingers'
    keys = []
    points = 0
    for i in range(4):
        for k in symbols[i]:
            if k == '.':
                continue
            keys.append(int(k))
    for i in range(1, 10):
        if 0 < keys.count(i) <= 2 * fingers:
            points += 1
    return points


def main():
    fingers = int(input())
    symbols = [str(input()) for i in range(4)]
    print(trainer(fingers, symbols))


if __name__ == "__main__":
    main()
