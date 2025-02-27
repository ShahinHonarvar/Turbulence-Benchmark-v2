def palindrome_of_length_at_least_n(input_string):
    input_string = input_string.lower()
    palindromes = set()
    for start_index in range(len(input_string)):
        for length in range(5, min(len(input_string) - start_index, 6)):
            substring = input_string[start_index:start_index + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes