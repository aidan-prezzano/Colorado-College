import cipher
'''
My plan is to have 2 functions: first the test_ciphers function which takes in the ciphered text and goes through each different way of decrypting. It first starts with the Atbash version
and then moves on to the Caesar one. In the Ceaser loops I want it to shift the line by 1 and increase every time until it gets to 15. If none of them come out as a real sentence then ill try
the weaved version but only if the length of the ciphered text is divisible by the amount it is getting weaved by. Once I figure out what method works I then move onto the next function. the
decrypt_scheme function runs the output of the code line by line. It checks if the index of the line is equal to one, if so then it runs the method that I found worked. Then it checks for two
and so on. Then I only display the decrypt_scheme function because that is all that is necessary for the output to run smoothly. 
'''
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

def decrypt_scheme():

    scheme_file = open('scheme.txt', 'r')

    for idx, ciphertext in enumerate(scheme_file):
        ciphertext = ciphertext.strip()
        #print('line #' + str(idx) + ': ' + ciphertext)
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
decrypt_scheme()

# **************************************************************************
'''
my strategy was to have a function for testing and a function for output and I think it worked pretty well. I liked this assignment because it make me think of different ways to decrypt and encrypt
the text. The most challenging part for me was trying to make the weave decrypt properly. I realized you had to take the length of the line which took some time to figure out. 
'''


