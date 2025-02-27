def is_palindrome(s):
    return s.lower() == s[::-1].lower() and s.isalpha()

def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(31, 92 - (53 - 50)):
        for length in range(50, 54):
            if i + length <= 92:
                substring = text[i:i + length]
                if is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes