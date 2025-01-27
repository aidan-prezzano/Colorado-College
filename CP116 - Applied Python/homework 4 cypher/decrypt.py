import cipher


# **************************************************************************


def test_ciphers(ciphertext):
    print('')
    print('------------------------')
    print('Atbash: ' + cipher.Atbash().decode(ciphertext))
    i = 0
    while i < 15:
        print(f'index {i} : {cipher.Caesar(i).decode(ciphertext)}')
        i += 1

    j = 1
    while j < 15:
        if len(ciphertext) % j == 0:
            print(f'index {j} : {cipher.Weave(j).decode(ciphertext)}')
            j += 1


# **************************************************************************


def decrpty_scheme():

    scheme_file = open('scheme.txt', 'r')

    for idx, ciphertext in enumerate(scheme_file):
        ciphertext = ciphertext.strip()
        #print('line #' + str(idx) + ': ' + ciphertext)
        if idx == 0:
            print(cipher.Caesar(3).decode(ciphertext))
        if idx == 1:
            print(cipher.Atbash().decode(ciphertext))
        if idx == 2:
            test_ciphers(ciphertext)
        if idx == 3:
           pass
        if idx == 4:
            print(cipher.Atbash().decode(ciphertext))
        if idx == 5:
            print(cipher.Caesar(12).decode(ciphertext))




    scheme_file.close()

# **************************************************************************


print('---------------------------------------')
decrpty_scheme()


# **************************************************************************


