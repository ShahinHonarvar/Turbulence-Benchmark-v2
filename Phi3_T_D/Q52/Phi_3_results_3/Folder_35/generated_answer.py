def palindrome_of_length_n(input_string):
    n = 116
    palindromes = set()
    lower_input_string = input_string.lower()
    for start_index in range(len(lower_input_string) - n + 1):
        substring = lower_input_string[start_index:start_index + n]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes