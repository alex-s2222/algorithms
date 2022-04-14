from random import randint


def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int((low + high)/2)
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


# end = int(input())
end = 100
mass = [randint(0, end) for i in range(end)]
mass = sorted(mass)

print(mass)
print(mass.index(48))
print(binary_search(mass, 48))

