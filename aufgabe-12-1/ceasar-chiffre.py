
# 1. Moduls einlesen
mode = ...

# 2. Nachricht einlesen
message = ...

# 3. Verschiebung (Shift) einlesen
shift = ...

# 4. Nachricht gemäss konfiguration verarbeiten
output = ceasar_chiffre(mode,message,shift)

# 5. Nachricht auf der Konsole ausgeben
print(output)

####

def ceasar_chiffre(mode,message,shift):
    result = ""
    # transverse the plain message
    for i in range(len(message)):
        char = message[i]

        # Encrypt uppercase characters in plain message
        if (char.isupper()):
            result += chr((ord(char) + shift*mode-65) % 26 + 65)
        # Encrypt lowercase characters in plain message
        else:
            result += chr((ord(char) + shift*mode-97) % 26 + 97)
    return result
