def selectionSort(data, sort_keys):
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            current_item = tuple(data[i][key] for key in sort_keys)
            next_item = tuple(data[j][key] for key in sort_keys)
            
            if current_item > next_item:
                data[i], data[j] = data[j], data[i]
    return data
def main():
    testList = [
        {'First Name': 'Hamza', 'Last Name': 'Farooqui'},
        {'First Name': 'Junaid', 'Last Name': 'Qamar'},
        {'First Name': 'Farooq', 'Last Name': 'Wajih'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Mohammad', 'Last Name': 'Ali'},
        {'First Name': 'Mohammad', 'Last Name': 'Ahmed'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Sheikh'},
        {'First Name': 'Shaheen', 'Last Name': 'Afridi'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Shahid', 'Last Name': 'Afridi'},
        {'First Name': 'Armaan', 'Last Name': 'Seth'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]
    test = selectionSort(testList , ['First Name' , 'Last Name']);

    print(test);

main()