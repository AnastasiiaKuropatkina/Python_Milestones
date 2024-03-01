def encrypt_caesar_shift(message: str, shift_key: int):
    encrypt_message = ''

    for char in message:
        if char.isalpha():
            # Convert character to the ASCII code.
            new_char_code = ord(char) + shift_key
            last_char = ord('Z') if char.isupper() else ord('z')
            if new_char_code > last_char:
                new_char_code -= 26
            new_char = chr(new_char_code)
            encrypt_message += new_char
        else:
            encrypt_message += char

    return encrypt_message, shift_key


user_message = input("Enter the message i.e to be encrypted: ")
user_shift_key = int(input("Enter the key to encrypt(integer): "))
encrypt_text = encrypt_caesar_shift(user_message, user_shift_key)
print(f"Encrypted Text: {encrypt_text}")
