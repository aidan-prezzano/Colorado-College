import math

# Provided for your use, should you so desire
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_REVERSED = ALPHABET[::-1]


# The base class doesn't do any useful encoding or decoding, it exists mostly to provide a
# centralized run_test to every cipher subclass you implement
class Cipher:
    def __init__(self):
        self.name = "Base Class"

    def encode(self, cleartext):
        return cleartext

    def decode(self, ciphertext):
        return ciphertext

    def run_test(self):
        # Here is a small handful of strings to test the encode and decode methods on
        # I've chosen strings that have different properties/characters, but a more robust test would
        # have an even wider variety of weird things that could show up in strings
        test_strings = [
            "Here is a very basic string with nothing unusual",
            "This one has punctuation!!! Good luck :)",
        ]



        # Iterate through each test string one by one, making sure that you get the same string back after
        # encoding and then decoding
        print(f"Testing {self.name:}")
        for cleartext in test_strings:
            # First, encode the string to get the ciphertext
            ciphertext = self.encode(cleartext)
            # Then, decode the cipher text to get back to the original cleartext
            decoded_message = self.decode(ciphertext)
            print(f"\t\tStarting text = '{cleartext}'")
            print(f"\t\tEncoded text  = '{ciphertext}'")
            print(f"\t\tDecoded text  = '{decoded_message}'")
            # My encoding implementations lowercase the cleartext, so I ignore capitals when checking
            if cleartext.lower() == decoded_message.lower():
                # If it matches exactly, then it's definitely working!
                print("\t✓ Match! Excellent")
            else:
                # If it doesn't match exactly it may still be correct, but the process corrupts the input
                # slightly, e.g. the Weave cipher may add padding characters
                print("\t𐄂 Decoded string does not match exactly. Please verify correctness.")
            print()
        print()


class Atbash(Cipher):
    def __init__(self):
        self.name = "Atbash"

    # iterate through each character in the clear text string
    # if the character is in the alphabet ...
    #   - find its position within the alphabet (ex: 'b' is in the 1st position)
    #   - find the character at this position in the alphabet reversed  (ex: 1st position in reversed alphabet is 'y')
    #   - add this character to the cipher text
    # else, add this non-alphabet character to the cipher text
    def encode(self, cleartext):
        ciphertext = ""
        for char in cleartext.lower():
            if char in ALPHABET:
                char_idx_in_alphabet = ALPHABET.index(char)
                char_at_idx_in_reversed_alphabet = ALPHABET_REVERSED[char_idx_in_alphabet]
                ciphertext += char_at_idx_in_reversed_alphabet
            else:
                ciphertext += char
        return ciphertext

    # as the logic to decode is the same to encode - call the encode function with the cipher text
    def decode(self, ciphertext):
        return self.encode(ciphertext)


class Caesar(Cipher):
    def __init__(self, n):
        # When initializing a Caesar Cipher, we need to specify the (integer) shift value for
        # this specific instance of a Caesar Cipher
        self.name = f"Caesar-{n}"
        self.shift = n

    # iterate through each character in the clear text string
    # if the character is in the alphabet ...
    #   - find its position within the alphabet (ex: 'b' is in the 1st position)
    #   - find the new position, which is current position + shift ... wrapping around the alphabet
    #   - add this character to the cipher text
    # else, add this non-alphabet character to the cipher text
    def encode(self, cleartext):
        ciphertext = ""
        for char in cleartext.lower():
            if char in ALPHABET:
                char_idx_in_alphabet = ALPHABET.index(char)
                new_idx = char_idx_in_alphabet + self.shift
                new_idx = (new_idx - 26) if (new_idx > 25) else new_idx
                char_at_new_idx = ALPHABET[new_idx]
                ciphertext += char_at_new_idx
            else:
                ciphertext += char
        return ciphertext

    # iterate through each character in the clear text string
    # if the character is in the alphabet ...
    #   - find its position within the alphabet (ex: 'b' is in the 1st position)
    #   - find the new position, which is current position - shift ... wrapping around the alphabet
    #   - add this character to the cipher text
    # else, add this non-alphabet character to the cipher text
    def decode(self, ciphertext):
        cleartext = ""
        for char in ciphertext.lower():
            if char in ALPHABET:
                char_idx_in_alphabet = ALPHABET.index(char)
                new_idx = char_idx_in_alphabet - self.shift
                new_idx = (new_idx + 26) if (new_idx < 0) else new_idx
                char_at_new_idx = ALPHABET[new_idx]
                cleartext += char_at_new_idx
            else:
                cleartext += char
        return cleartext


class Weave(Cipher):
    def __init__(self, n):
        # Similar to a Caesar Cipher, each instance of a Weave Cipher will get set to a specific
        # number of splits when it's initialized
        self.name = f"{n}-Weave"
        self.size = n

    def encode(self, cleartext):
        ciphertext = ""

        # find the character size of each splice (rounding up)
        # as ex: if cleartext length = 48, while # splices = 3 ...  splice size = 16 (16x3=48)
        # as ex: if cleartext length = 40, while # splices = 3 ...  splice size = 14 (14x3=42)
        nbr_cleartext_splice_size = math.ceil(len(cleartext) / self.size)

        # splice the cleartext to the specified #
        # as ex: 'This one has punctuation!!! Good luck :)', length of 40 with 3 splices, creates a list of:
        #  (1): 'This one has p'
        #  (2): 'unctuation!!! '
        #  (3): 'Good luck :)'
        splice_txts = []
        for splice_nbr in range(0, self.size):
            splice_x = splice_nbr * nbr_cleartext_splice_size
            splice_y = splice_x + nbr_cleartext_splice_size
            splice_txt = cleartext[splice_x:splice_y]
            splice_txts.append(splice_txt)

        # for each splice size (idx) (ex: idx = 0...13 when cleartext = 'This one has punctuation!!! Good luck :)')
        # for each splice text (jdx) (ex: jdx = 0...2 'This one has p', 'unctuation!!! ', 'Good luck :)  '
        # add the char at position jdx, idx into the cypher, ex: TuGhno ...
        # in the case where there does not exist a char / value at jdx, idx ... use '@'
        for idx in range(0, nbr_cleartext_splice_size):
            for jdx in range(0, len(splice_txts)):
                if idx < len(splice_txts[jdx]):
                    ciphertext += splice_txts[jdx][idx]
                else:
                    ciphertext += '@'

        return ciphertext

    def decode(self, ciphertext):
        cleartext = ""

        # find the character size of each splice (rounding up)
        # as ex: if cleartext length = 48, while # splices = 3 ...  splice size = 16 (16x3=48)
        # as ex: if cleartext length = 40, while # splices = 3 ...  splice size = 14 (14x3=42)
        nbr_cleartext_splice_size = math.ceil(len(ciphertext) / self.size)

        # for the number of splices (idx) (ex: 3)
        # for each splice size (jdx) (ex: jdx = 0...13 when cleartext = 'This one has punctuation!!! Good luck :)')
        # calculate the char index (ex: 0,3,6,9,12,15,18,21,24,27,30,33,36,39,1,4,7,10 ...)
        # get the char at the encoded text ... if '@' set to blank
        # add the char to the cleartext string
        for idx in range(0, self.size):
            for jdx in range(0, nbr_cleartext_splice_size):
                char_idx = (jdx * self.size) + idx
                char = ciphertext[char_idx]
                if ciphertext[char_idx] == '@':
                    char = ''
                cleartext += char

        return cleartext


ciphers = [
    Cipher(),
    Atbash(),
    Caesar(3),
    Caesar(13),
    Weave(2),
    Weave(3)
]

print("This program implements several different ciphers that can be used to encode/decode text.")
print("Here is a sampling of ciphers to showcase the options.")

# After you have finished implementing the Atbash, Caesar, and Weave ciphers this code will instantiate and
# test a few of each to make sure they're working correctly. Inspect the output to verify for yourself!
for cipher in ciphers:
    cipher.run_test()
