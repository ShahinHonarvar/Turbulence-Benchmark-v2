def is_palindrome(s):
    return s == s[::-1] and s.isalpha()

def palindromes_of_specific_lengths(input_string):
    result = set()
    for length in range(154, 183):
        for i in range(101, 293 - length + 1):
            substring = input_string[i:i + length].lower()
            if is_palindrome(substring):
                result.add(substring)
    return result