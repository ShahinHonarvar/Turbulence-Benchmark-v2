def palindrome_of_length_n(input_string):
    palindromes = set()
    lower_string = input_string.lower()
    for i in range(len(lower_string) - 416 + 1):
        substring = lower_string[i:i + 416]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes