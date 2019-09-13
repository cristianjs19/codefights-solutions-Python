def permutationCipher(password, key):
    table = key.maketrans(string.ascii_lowercase, key)
    return password.translate(table)