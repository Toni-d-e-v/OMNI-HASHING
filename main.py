# OMNI HASH ALOGRITHM
# Simple 48 byte hash algorithm, 
# Author: Toni Dumancic
# Version: 1.0

import random

def rot(text,size):
    text = list(text)
    new_text = []
    for i in range(0, len(text)):
        new_text.append(text[(i+size)%len(size)])
    new_text = ''.join(new_text)
    return new_text
def hash_function(string):
    byte_array = []
    for i in range(0, len(string)):
        byte_value = ord(string[i])
        byte_array.append(byte_value)
    pre_size = len(byte_array)
    for i in range(0, len(byte_array)):
        if len(byte_array) < 48:
            while len(byte_array) < 48:
                for byte in range(0, len(byte_array)):
                    byte_array.append(byte_array[byte] + pre_size)   
        elif len(byte_array) > 48:
            byte_array = byte_array[:48]
    for i in range(0, len(byte_array)):
        byte_array[i] = hex(byte_array[i])
    byte_array = ''.join(byte_array)
    byte_array = byte_array.replace("0x", "")
    return rot(byte_array, pre_size)
def test_hash_function():
    print("Test hash function")
    print(hash_function("Hello World"))
    print("TEST FOR PROOF OF WORK")
    proof_of_work()
def proof_of_work():
    while True:
        rand_num = random.randint(0, 200000)
        hash = hash_function(str(rand_num))
        print(hash)
        if hash.startswith("0"):
            print("Found hash")
            print(hash)
            break
test_hash_function()
