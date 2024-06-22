def encode_to_binary(input_string):
    # Encode a string into binary representations
    binary_output = [format(ord(char), '07b') for char in input_string]
    return binary_output

# Example usage
input_string = "Don't mind"

# Encode the input string into binary representations
binary_output = encode_to_binary(input_string)

# Print the binary output, each binary representation on a new line
print(*binary_output, sep='\n')
