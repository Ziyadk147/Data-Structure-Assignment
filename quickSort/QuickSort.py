def quick_sort(arr, low, high):
    if low < high:
        p = hoare_partition(arr, low, high)
        quick_sort(arr, low, p)
        quick_sort(arr, p + 1, high)
def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
def main():
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("Original array:", arr)
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
main()