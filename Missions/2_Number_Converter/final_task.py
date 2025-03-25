# Code created & optimised by Avner
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGIT_MAP = {d: i for i, d in enumerate(DIGITS)}

def decimal_to_base(decimal, base):
    if decimal == 0:
        return "0"
    result = []
    while decimal:
        decimal, digit = divmod(decimal, base)
        result.append(DIGITS[digit])
    return ''.join(reversed(result))

def base_to_decimal(number, base):
    value = 0
    for digit in number:
        value = value * base + DIGIT_MAP[digit.upper()]
    return value

def validate_number(number, base):
    valid = set(DIGITS[:base])
    return all(digit.upper() in valid for digit in number)

def display_menu():
    print("Number Converter")
    print("1. Convert from decimal to binary")
    print("2. Convert from binary to decimal")
    print("3. Convert between binary, octal, and hexadecimal")
    print("4. Convert between any numeral systems")
    print("5. Quit")

def get_valid_choice(prompt, min_value, max_value):
    while True:
        choice = input(prompt)
        if choice.isdigit():
            choice = int(choice)
            if min_value <= choice <= max_value:
                return choice
        print("Invalid choice. Please try again.")

def get_valid_number(prompt, base):
    while True:
        number = input(prompt)
        if validate_number(number, base):
            return number
        print(f"Invalid number for base {base}. Please try again.")

def main():
    while True:
        display_menu()
        choice = get_valid_choice("Enter your choice: ", 1, 5)
        
        if choice == 1:
            decimal = int(get_valid_number("Enter a decimal number: ", 10))
            print(f"Binary: {decimal_to_base(decimal, 2)}")
            
        elif choice == 2:
            binary = get_valid_number("Enter a binary number: ", 2)
            print(f"Decimal: {base_to_decimal(binary, 2)}")
            
        elif choice == 3:
            base_from = get_valid_choice("Enter the base of the number (2, 8, 16): ", 2, 16)
            number = get_valid_number(f"Enter a base {base_from} number: ", base_from)
            decimal = base_to_decimal(number, base_from)
            base_to = get_valid_choice("Enter the base to convert to (2, 8, 16): ", 2, 16)
            print(f"Result: {decimal_to_base(decimal, base_to)}")
            
        elif choice == 4:
            base_from = get_valid_choice("Enter the base of the number (2-36): ", 2, 36)
            number = get_valid_number(f"Enter a base {base_from} number: ", base_from)
            decimal = base_to_decimal(number, base_from)
            base_to = get_valid_choice("Enter the base to convert to (2-36): ", 2, 36)
            print(f"Result: {decimal_to_base(decimal, base_to)}")
            
        else:
            print("Thank you for using the Number Converter!")
            break

if __name__ == "__main__":
    main()
