# File-Compression-Using-Huffman-Coding
This code implements file compression using Huffman coding, a popular algorithm for lossless data compression. It allows you to compress a text file into a binary file and then decompress the binary file back to its original text format.

The code first prompts the user to enter the file path of the text file they want to compress. It then builds a frequency library by counting the occurrences of each character in the text.

Using a heap data structure, the code constructs a Huffman tree based on the character frequencies. The Huffman tree is used to generate variable-length codes for each character, forming a dictionary of Huffman codes.

The text file is then read again, and the text is encoded using the Huffman codes. The encoded text is stored in a binary file named "compressed_file.bin", representing the compressed version of the original text file.

To decompress the file, the code reads the binary file, removes the padding, and decodes the text using the Huffman dictionary. The decoded text is written to a new file named "decompressed.txt", which represents the reconstructed original text.

This code provides a basic implementation of file compression using Huffman coding and can serve as a starting point for further exploration and optimization.
