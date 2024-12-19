def from_dec_to_else(n1, incoming_base, output_base):
    hex_digits = "0123456789ABCDEF"
    n1 = int(n1)
    n2 = str()
    while n1 > 0:
        ost = n1 % output_base #остаток
        n2 = hex_digits[ost] + n2 #добавляем остаток
        n1 //= output_base
    return n2

def from_else_to_dec(n1, incoming_base, output_base):
    hex_digits = "0123456789ABCDEF"
    n1 = n1[::-1].upper()
    n2 = int()
    for i in range(len(n1)):
        n2 += hex_digits.index(n1[i]) * incoming_base ** i
    return n2
def convert(n1, incoming_base, output_base):
    if incoming_base == 10: #из 10 в любую
        n2 = from_dec_to_else(n1, incoming_base, output_base)
        return n2
    elif output_base == 10:        #из 10 в любую
        n2 = from_else_to_dec(n1, incoming_base, output_base)
        return n2
    else:
        n2 = from_else_to_dec(n1, incoming_base, output_base)
        n2 = from_dec_to_else(n2, incoming_base, output_base)
        return n2


def main():
    hex_digits = "0123456789ABCDEF"
    n1 = input("Введи целое неотрицательное число: ").upper()    #входящее число
    for i in range(len(n1)):
        if n1[i] not in hex_digits:
            n1 = input("Введи целое неотрицательное число: ")
            break
    while "." in n1:
        n1 = input("Введи целое неотрицательное число: ")
    incoming_base = int(input("Введи сс: "))
    while not isinstance(incoming_base, int):
        incoming_base = int(input("Введи сс: "))
    output_base = int(input("Введи в какую сс: "))
    while not isinstance(output_base, int):
        output_base = int(input("Введи в какую сс: "))
    n2 = convert(n1, incoming_base, output_base)
    print("Вывод: ", n2)

if __name__ == "__main__":
    main()