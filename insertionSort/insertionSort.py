def running_median_insertion_sort(stream):
    sorted_list = []
    for number in stream:
        inserted = False
        for i in range(len(sorted_list)):
            if number < sorted_list[i]:
                sorted_list.insert(i, number)
                inserted = True
                break
        if not inserted:
            sorted_list.append(number)
        
        n = len(sorted_list)
        if n % 2 == 1:  
            median = sorted_list[n // 2]
        else:  
            median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2

        print(f"Current median: {median}")

def main():
    numbers = [2, 1, 5, 7, 2, 0, 5]
    running_median_insertion_sort(numbers)

main()