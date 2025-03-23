def W3X(message, key, direction=1):
    key_index = 0
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '0123456789'
    final_message = ''

    for char in message:
        if char in alphabet_lower:  
            current_alphabet = alphabet_lower
        elif char in alphabet_upper:  
            current_alphabet = alphabet_upper
        else:  
            final_message += char
            continue  

        key_char = key[key_index % len(key)]
        key_index += 1

        if key_char in alphabet_lower:
            offset = alphabet_lower.index(key_char.lower())  
        elif key_char in number:
            offset = number.index(key_char)
        else:
            offset = 0

        index = current_alphabet.find(char)
        new_index = (index + offset * direction) % len(current_alphabet)
        final_message += current_alphabet[new_index]

    return final_message

def encrypt(message, key):
    return W3X(message, key)

def decrypt(message, key):
    return W3X(message, key, -1)

while True:
    language = input('Italiano/English? (IT/EN): ').strip().lower()

    if language in ['it', 'en']:
        break
    print("Scelta non valida. Inserisci 'IT' per Italiano o 'EN' per inglese./nInvalid choice. Enter 'IT' for Italian or 'EN' for English.")

if language == 'it':
    while True:
        operation = input("Vuoi criptare o decriptare? (c/d) o uscire (e): ").strip().lower()

        while operation not in ["c", "d", "e"]:
            print("Scelta non valida. Inserisci 'c' per criptare o 'd' per decriptare o 'q' per uscire.")
            operation = input("Vuoi criptare o decriptare? (c/d) o uscire (e): ").strip().lower()

        if operation == "e":
            print('\nSviluppato da W3X - Raffaele Brancaccio\nInfo e contatti https://linktr.ee/wolfl3x\n')
            break

        elif operation == "c":
            text = input("Inserisci il testo da criptare: ")
            custom_key = input("Inserisci la chiave di codifica: ")
            result = encrypt(text, custom_key)
            print(f"\nTesto criptato: {result}\n")
            
        elif operation == "d":
            text = input("Inserisci il testo da decriptare: ")
            custom_key = input("Inserisci la chiave di codifica: ")
            result = decrypt(text, custom_key)
            print(f"\nTesto decriptato: {result}\n")
            


if language == "en":
    while True:
        operation = input("Do you want to encrypt or decrypt? (e/d) or exit (q): ").strip().lower()

        while operation not in ["e", "d", "q"]:
            print("Invalid choice. Enter ‘e’ to encrypt or ‘d’ to decrypt or ‘q’ to exit.")
            operation = input("Do you want to encrypt or decrypt? (c/d) or exit (q): ").strip().lower()

        if operation == "q":
            print('\nDeveloped by W3X - Raffaele Brancaccio\nInfo and contacts https://linktr.ee/wolfl3x\n')
            break

        elif operation == "e":
            text = input("Enter the text to be encrypted: ")
            custom_key = input("Enter the encryption key: ")
            result = encrypt(text, custom_key)
            print(f"\nEncrypted text: {result}\n")
            
        elif operation == "d":
            text = input("Enter the text to be decrypted: ")
            custom_key = input("Enter the encryption key: ")
            result = decrypt(text, custom_key)
            print(f"\nDecrypted text: {result}\n")