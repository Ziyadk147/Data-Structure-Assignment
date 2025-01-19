def bubbleSort(elements , key):
    for i in range(len(elements) ):
        isSwapped = False;
        for j in range(len(elements)  - i - 1):
            firstElement = elements[ j ][ key ]
            secondElement = elements[ j + 1 ][ key ]
            if firstElement > secondElement:
                elements[j] , elements[j+1] = elements[j+1] , elements[j]
                isSwapped = True;
        if isSwapped == False:
            break;

def main():
    testElem = [
        { 'name': 'Hamza', 'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'Hasnain', 'transaction_amount': 400, 'device': 'google pixel'},
        { 'name': 'Palwasha', 'transaction_amount': 200, 'device': 'vivo'},
        { 'name': 'Aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]

    bubbleSort(testElem , 'device');
main()