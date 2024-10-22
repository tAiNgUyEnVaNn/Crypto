def ksa(key):
    print('Key Scheduling')
    key_length = len(key)
    S = list(range(8))
    j = 0
    for i in range(8):
        j = (j + S[i] + key[i % key_length]) % 8
        S[i], S[j] = S[j], S[i]
        print(i, j, 's{}'.format(i), S)
    return S

def prga(S):
    print('Encrypt: ')
    i = 0
    j = 0
    while True:
        i = (i + 1) % 8
        j = (j + S[i]) % 8
        temp = S[i]
        S[i] = S[j]
        S[j] = temp
        # print(S)
        K = S[(S[i] + S[j]) % 8]
        print(i, j, S, K)
        yield K

def rc4(key, plaintext):
    key = [ord(c) for c in key]
    S = ksa(key)
    keystream = prga(S)
    ciphertext = [chr(ord(c) ^ next(keystream)) for c in plaintext]
    return ''.join(ciphertext)

# Example usage
key = "1236"
plaintext = "1222"
ciphertext = rc4(key, plaintext)
print(f"Ciphertext: {ciphertext}")

# Decrypting (RC4 is symmetric, so we use the same function)
decrypted_text = rc4(key, ciphertext)
print(f"Decrypted text: {decrypted_text}")
