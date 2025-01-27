import cipher

# **************************************************************************


def test_ciphers(ciphertext):
    print('')
    print('------------------------')
    print('Atbash: ' + cipher.Atbash().decode(ciphertext))
    for idx in range(1, 15):
        print('Caesar (' + str(idx) + '): ' + cipher.Caesar(idx).decode(ciphertext))
        if len(ciphertext) % idx == 0:
            print('Weave (' + str(idx) + '): ' + cipher.Weave(idx).decode(ciphertext))


# **************************************************************************

def run_test():

    scheme_file = open('scheme.txt', 'r')

    for idx, ciphertext in enumerate(scheme_file):
        ciphertext = ciphertext.strip()
        if idx == 0:
            print(cipher.Caesar(3).decode(ciphertext))
        if idx == 1:
            print(cipher.Atbash().decode(ciphertext))
        if idx == 2:
            print(cipher.Weave(3).decode(ciphertext))
        if idx == 3:
            print(cipher.Weave(6).decode(ciphertext))
        if idx == 4:
            print(cipher.Atbash().decode(ciphertext))
        if idx == 5:
            print(cipher.Caesar(12).decode(ciphertext))

    scheme_file.close()

# **************************************************************************


print('---------------------------------------')
run_test()


# **************************************************************************

