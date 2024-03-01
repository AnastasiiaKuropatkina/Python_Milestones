def receive_positive_info():
    while True:
        try:
            user_message = input("Enter the message i.e to be decrypted: ")
            user_shift_key = int(input("Enter the key to decrypt(integer): "))
                return user_shift_key, user_message
        except ValueError as exception:
            print(exception)

def decrypt_caesar_shift(message: str, shift_key: int):
    receive_positive_info()
    decrypt_message = ''

    for char in message:
        if char.isalpha():
            # Convert character to the ASCII code.
            new_char_code = ord(char) - shift_key
            first_char = ord('A') if char.isupper() else ord('a')
            if new_char_code < first_char:
                new_char_code += 26
            new_char = chr(new_char_code)
            decrypt_message += new_char
        else:
            decrypt_message += char

    return decrypt_message

decrypt_text = decrypt_caesar_shift(user_message, user_shift_key)
print(f"Decrypted Text: {decrypt_text}")




def get_positive_number():
    while True:  # Loop indefinitely until a valid input is received
        try:
            x = int(input('Enter an integer number: '))
            return x  # Return the number if it is successfully converted to an integer
        except ValueError:  # Catch the ValueError if the conversion fails
            print("That was not an integer. Please try again.")  # Inform the user
            # The loop will then continue, giving the user another chance to input a valid integer

# Call the function
number = get_positive_number()
print(f"You entered: {number}")