def palindrome_of_length_at_least_n(input_string):
    palindromes = set()
    chars = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(input_string)):
        for length in range(150, len(input_string) - i + 1):
            substring = input_string[i:i + length]
            if all((c.lower() in chars for c in substring)) and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes