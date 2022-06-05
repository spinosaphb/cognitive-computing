

def get_cardinal(number: int) -> int:

    cardinal = 0
    while number > 0:
        rest = number % 2
        if rest == 1:
            cardinal += 1
        number //= 2
    
    return cardinal


def main():
    list_ = []
    while True:
        elem = input()
        if elem == '':
            break
        list_.append(int(elem))
    
    values = [(elem, get_cardinal(elem)) for elem in list_]

    #sorted(values, key=1)
    elem_sorted = sorted(values, key=lambda elem: elem[1])
    values = list(map(lambda elem: elem[0], elem_sorted))
    print(values)

if __name__ == '__main__':
    main()