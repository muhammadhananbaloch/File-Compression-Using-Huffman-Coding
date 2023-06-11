from heapq import heappush, heappop, heapify
from collections import defaultdict
from bitarray import bitarray
import time

print("File Compression Using Huffman Coding".center(100))
# Get the file path from the user

while True:
    text = input("Enter the file path: ")
    try:
        with open(text) as fil:  # with open closes the file automatically after opening
            break
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission Denied!")


def display_message(message, duration):
    print(message)
    time.sleep(duration)


display_message('Compressing File...', 1)

freq_lib = defaultdict(int)  # generate a default library
with open(text, 'r') as file:
    for line in file:
        for ch in line.strip():  # count each character and record into the frequency library
            freq_lib[ch] += 1

heap = [[fq, [sym, ""]] for sym, fq in freq_lib.items()]  # '' is for entering the Huffman code later

heapify(heap)  # transform the list into a heap tree structure

while len(heap) > 1:
    right = heappop(heap)  # heappop - Pop and return the smallest item from the heap

    left = heappop(heap)

    for pair in right[1:]:
        pair[1] = '0' + pair[1]  # add zero to all the right nodes
    for pair in left[1:]:
        pair[1] = '1' + pair[1]  # add one to all the left nodes
    heappush(heap, [right[0] + left[0]] + right[1:] + left[1:])  # add values onto the heap

huffman_list = right[1:] + left[1:]

huffman_dict = {a[0]: bitarray(str(a[1])) for a in huffman_list}

encoded_text = bitarray()
with open(text, 'r') as file:
    for line in file:
        encoded_text.encode(huffman_dict, line.strip())

padding = 8 - (len(encoded_text) % 8)
with open('compressed_file.bin', 'wb') as w:
    encoded_text.tofile(w)

decoded_text = bitarray()

with open('compressed_file.bin', 'rb') as r:
    decoded_text.fromfile(r)

display_message('File Successfully Compressed!', 0.5)

display_message('Decompressing File...', 1)

decoded_text = decoded_text[:-padding]  # remove padding

decoded_text = decoded_text.decode(huffman_dict)
decoded_text = ''.join(decoded_text)

display_message('File Successfully Decompressed!', 0.5)
print(f'Decompressed text is: {decoded_text}')

with open('decompressed.txt', 'w') as w:
    w.write(decoded_text)
