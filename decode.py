def decode_from_binary(binary_strings):
    # Decode a list of binary strings back into the original string
    decoded_string = ''.join(chr(int(binary, 2)) for binary in binary_strings)
    return decoded_string

# Sample binary output for decoding
binary_input = """1000100
1101111
1101110
0100111
1110100
0100000
1101101
1101001
1101110
1100100"""

# Split the binary input into a list of binary strings
binary_list = binary_input.splitlines()

# Decode the binary representation back into the original string
decoded_string = decode_from_binary(binary_list)

# Print the decoded string
print(decoded_string)
