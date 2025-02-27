def palindrome_of_length_at_least_n(input_string):
    input_string = input_string.lower()
    palindromes = set()
    n = 144
    length = len(input_string)
    for i in range(length):
        for j in range(i + n, length + 1):
            substring = input_string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes