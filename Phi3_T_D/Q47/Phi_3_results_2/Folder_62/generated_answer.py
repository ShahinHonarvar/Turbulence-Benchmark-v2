def is_letter(char):
    return 'A' <= char <= 'Z' or 'a' <= char <= 'z'

def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def palindromes_of_specific_lengths(input_string):
    start, end = (26, 87)
    palindromes = set()
    for length in range(52, 57):
        for i in range(start, end - length + 1):
            substring = input_string[i:i + length]
            if all((is_letter(char) for char in substring)) and is_palindrome(substring):
                palindromes.add(substring.lower())
    return palindromes