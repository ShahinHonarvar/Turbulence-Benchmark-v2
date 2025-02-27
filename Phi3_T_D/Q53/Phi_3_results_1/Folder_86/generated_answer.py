def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(input_str):
    length = 133
    palindromes = set()
    input_str = input_str.lower()
    for i in range(len(input_str)):
        for j in range(i + length, len(input_str) + 1):
            substring = input_str[i:j]
            if len(substring) >= length and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes