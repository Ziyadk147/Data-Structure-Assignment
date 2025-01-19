def merge_sort(arr, key, descending=False):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid] 
        right_half = arr[mid:]
        merge_sort(left_half, key, descending)
        merge_sort(right_half, key, descending)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if (left_half[i][key] < right_half[j][key] and not descending) or \
               (left_half[i][key] > right_half[j][key] and descending):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1



elements = [
    {'name': 'Riley', 'age': 17, 'time_hours': 1},
    {'name': 'Jimmy', 'age': 12, 'time_hours': 3},
    {'name': 'Zack', 'age': 21, 'time_hours': 2.5},
    {'name': 'Mike', 'age': 24, 'time_hours': 1.5},
]

merge_sort(elements, key='time_hours', descending=True)
print("Sorted by time_hours (descending):")
for athlete in elements:
    print(athlete)

merge_sort(elements, key='name', descending=False)
print("\nSorted by name (ascending):")
for athlete in elements:
    print(athlete)
