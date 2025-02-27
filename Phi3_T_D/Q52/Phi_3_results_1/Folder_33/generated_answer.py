def palindrome_of_length_n(input_string):
    n = 475
    set_of_palindromes = set()
    input_string = input_string.lower()
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if substring == substring[::-1]:
            set_of_palindromes.add(substring)
    return set_of_palindromes