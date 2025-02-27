def palindrome_of_length_n(input_string):
    palindromes = set()
    n = 100
    input_string = input_string.lower()
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes