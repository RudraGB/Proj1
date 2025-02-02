def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1,number):
        binary = bin(i)
        hexa = hex(i).upper()
        octal = oct(i)
        #(i,hexa[2:],octal[2:],binary[2:])
        print(f"{i:>{width}} {hexa[2:]:>{width}} {octal[2:]:>{width}} {binary[2:]:>{width}}")
       
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)