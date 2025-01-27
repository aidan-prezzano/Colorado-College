import cipher


# **************************************************************************


def test_ciphers(ciphertext):
    print('')
    print('------------------------')
    print('Atbash: ' + cipher.Atbash().decode(ciphertext))


# **************************************************************************


def decrpty_scheme():

    scheme_file = open('scheme.txt', 'r')

    for idx, ciphertext in enumerate(scheme_file):
        ciphertext = ciphertext.strip()
        #print('line #' + str(idx) + ': ' + ciphertext)
        if idx == 0:
            test_ciphers(ciphertext)

    scheme_file.close()

# **************************************************************************


print('---------------------------------------')
decrpty_scheme()


# **************************************************************************


