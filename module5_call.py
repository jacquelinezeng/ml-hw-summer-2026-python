from module5_mod import NumberList


def main():
    n=int(input('Enter N, a positive integer: '))

    data=NumberList()
    data.initialize_data(n)

    x=int(input('Enter X to search for: '))

    result=data.search_number(x)
    print(result)

main()