def average(array):
    # your code goes here
    averege = sum(set(array))/len(set(array))
    return averege

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
