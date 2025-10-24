def getPivot(number):
    average = sum(number) / len(number)
    pivot = number[0]
    mindiff = abs(number[0] - average)
    for i in number:
        diff = abs(i - average)
        if diff < mindiff:
            mindiff = diff
            pivot = i
    return pivot

def split(number):
    sub1 = []
    sub2 = []
    pivot = getPivot(number)
    for i in number:
        if i <= pivot:
            sub1.append(i)
        else:
            sub2.append(i)
    
    return sub1 + [pivot] + sub2


def main():
    # number = list(map(int, input().split()))
    number = [65, 15, 10, 20, 40, 55]
    number = split(number)
    print(number)


if __name__ == '__main__':
    main()
