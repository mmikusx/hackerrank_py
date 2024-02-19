def average(array):
    sum = 0
    for element in set(array):
        sum += element

    return sum / len(set(array))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)