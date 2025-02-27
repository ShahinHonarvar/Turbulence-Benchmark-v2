def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    n = 173
    palindromes = set()
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes