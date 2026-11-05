import random

comparisons = 0

# Partition function
def partition(a, low, high):
    global comparisons

    pivot = a[high]
    i = low - 1

    comparisons += 1

    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[high] = a[high], a[i + 1]

    return i + 1


# Deterministic Quick Sort
def quickSort(a, low, high):
    if low < high:
        p = partition(a, low, high)

        quickSort(a, low, p - 1)
        quickSort(a, p + 1, high)


# Randomized Quick Sort
def randomizedQuickSort(a, low, high):
    if low < high:

        # Select random pivot
        r = random.randint(low, high)

        a[r], a[high] = a[high], a[r]

        p = partition(a, low, high)

        randomizedQuickSort(a, low, p - 1)
        randomizedQuickSort(a, p + 1, high)


# Main program
n = int(input("Enter number of elements: "))

a = list(map(int, input("Enter array elements: ").split()))

b = a.copy()

# Deterministic Quick Sort
comparisons = 0
quickSort(a, 0, n - 1)

print("\nDeterministic Quick Sort:", a)
print("Deterministic Comparisons:", comparisons)

# Randomized Quick Sort
comparisons = 0
randomizedQuickSort(b, 0, n - 1)

print("\nRandomized Quick Sort:", b)
print("Randomized Comparisons:", comparisons)