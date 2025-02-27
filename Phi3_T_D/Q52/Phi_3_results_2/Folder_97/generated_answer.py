def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    length = 210
    palindromes = set()
    for i in range(len(input_string) - length + 1):
        substring = input_string[i:i + length]
        if substring.isalpha():
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes