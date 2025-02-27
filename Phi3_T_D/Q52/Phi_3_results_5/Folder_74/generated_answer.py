def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_n(input_string):
    input_lower = input_string.lower()
    palindromes = set()
    for i in range(len(input_lower) - 95):
        substring = input_lower[i:i + 96]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes