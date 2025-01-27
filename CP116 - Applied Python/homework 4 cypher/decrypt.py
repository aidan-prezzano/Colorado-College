import cipher

scheme_file = open('scheme.txt', 'r')

'''
def test_cipher():
    counter = 0
    lines = scheme_file.readlines[0:counter]
    print(lines)
    for line in lines:
        print(line)
        counter += 1
'''






for idx, ciphertext in enumerate(scheme_file):
    ciphertext = ciphertext.strip()
    first_line = scheme_file.readline()
    print(first_line)







#test_cipher()

scheme_file.close()





