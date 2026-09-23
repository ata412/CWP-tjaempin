import sys
if len(sys.argv) != 1:
    print("none")
else:
    table = 0
    while table <= 10:
        print(f"Table de {table}:", end=" ")
        number = 0
        while number <= 10:
            print(table * number, end="")
            if number < 10:
                print(" ", end="")
            number += 1
        print()
        table += 1