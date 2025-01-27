import math
# Provided for your use, should you so desire
from operator import index

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

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
    # if char in ALPHABET
    # new letter = 25 - the index that it is at in ALPHABET, set letter to new letter
    # print and add the converted character to the ciphertext
    # else add the original character in ciphertext such as a space
    def encode(self, cleartext):
        ciphertext = ""
        for char in cleartext.lower():
            if char in ALPHABET:
                new_char = 25 - (ALPHABET.index(char))
                final_char = ALPHABET[new_char]
                ciphertext += final_char
            else:
                ciphertext += char

        return ciphertext
    # Run encode because it basically puts the alphabet in reverse: allows you to run it again to decode
    def decode(self, ciphertext):
        cleartext = ""
        return  self.encode(ciphertext)


class Caesar(Cipher):
    def __init__(self, n):
        # When initializing a Caesar Cipher, we need to specify the (integer) shift value for
        # this specific instance of a Caesar Cipher
        self.name = f"Caesar-{n}"
        self.shift = n

    #
    # shift the character by that integer to the right
    # if the index becomes greater than 25 have it start back down at 0
    # change the char from and index to letter in alphabet
    # add char to ciphertext
    # if char has a space or char not in alphabet proceed as normal
    def encode(self, cleartext):
        ciphertext = ""
        for char in cleartext.lower():
            if char in ALPHABET:
                new_char_idx = self.shift + ALPHABET.index(char)
                if new_char_idx > 25:
                    new_char_idx = (new_char_idx - 26)

                final_char = ALPHABET[new_char_idx]
                ciphertext += final_char
            else:
                ciphertext += char

        return ciphertext

    # shift the char the other way
    # if char becomes less than 0, add 26 to the index
    # convert char from index to a real letter from alphabet
    # add the char's to cleartext and proceed as normal if letter is not in alphabet
    def decode(self, ciphertext):
        cleartext = ""
        for char in ciphertext.lower():
            if char in ALPHABET:
                new_char_idx = ALPHABET.index(char) - self.shift
                if new_char_idx < 0:
                    new_char_idx = (new_char_idx + 26)

                final_char = ALPHABET[new_char_idx]
                cleartext += final_char
            else:
                cleartext += char



        return cleartext


class Weave(Cipher):
    def __init__(self, n):
        # Similar to a Caesar Cipher, each instance of a Weave Cipher will get set to a specific
        # number of splits when it's initialized
        self.name = f"{n}-Weave"
        self.size = n

    # split text into self.size
    # pick first index of one first split and then second... so on
    #

    def encode(self, cleartext):

        ciphertext = ""

        # find the character size of each splice (rounding up)
        # as ex: if cleartext length = 48, while # splices = 3 ...  splice size = 16 (16x3=48)
        # as ex: if cleartext length = 40, while # splices = 3 ...  splice size = 14 (14x3=42)
        spliced_text_size = math.ceil(len(cleartext) / self.size)
        print(spliced_text_size)


        sliced_texts = [
            cleartext[i * spliced_text_size:(i + 1) * spliced_text_size]
            for i in range(self.size)
        ]

        counter = 0
        #new_list_of_sliced_texts = list_of_sliced_texts.split(',')
        while counter < spliced_text_size:
            for spliced_txt in sliced_texts:
                if counter < len(spliced_txt):
                    ciphertext += spliced_txt[counter]

                else:
                    ciphertext += '@'
            counter += 1


        return ciphertext

    def decode(self, ciphertext):
        # TODO: Implement decoding method for Weave Cipher
        cleartext = ""

        spliced_text_size = math.ceil(len(ciphertext) / self.size)

        counter_self_size = 0
        counter_spliced_text_size = 0
        position = 0
        # set counter = 0
        # once counter is great than spliced text stop
        # for text inside ciphertext
        while counter_self_size < self.size:
            while counter_spliced_text_size < spliced_text_size:
                final_char = ciphertext[position]
                cleartext += final_char
                position += self.size
                counter_spliced_text_size += 1

            counter_self_size += 1
            counter_spliced_text_size = 0
            position = 0 + counter_self_size



        return cleartext


ciphers = [
    Cipher(),
    Atbash(),
    Caesar(3),
    Caesar(13),
    Weave(2),
    Weave(3)
]

ciphers = [
    Caesar(3)
]

print("This program implements several different ciphers that can be used to encode/decode text.")
print("Here is a sampling of ciphers to showcase the options.")

# After you have finished implementing the Atbash, Caesar, and Weave ciphers this code will instantiate and
# test a few of each to make sure they're working correctly. Inspect the output to verify for yourself!
for cipher in ciphers:
    cipher.run_test()