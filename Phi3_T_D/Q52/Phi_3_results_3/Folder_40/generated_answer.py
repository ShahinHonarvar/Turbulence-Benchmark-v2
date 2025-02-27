def palindrome_of_length_n(input_string):
    length = 3
    palindromes = {input_string[i:i + length].lower() for i in range(len(input_string) - length + 1) if input_string[i:i + length].lower() == input_string[i:i + length].lower()[::-1] and input_string[i:i + length].isalpha()}
    return palindromes