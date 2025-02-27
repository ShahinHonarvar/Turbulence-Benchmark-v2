def is_palindrome(s):
    s = ''.join((c for c in s if c.isalpha())).lower()
    return s == s[::-1]

def palindromes_of_specific_lengths(text):
    relevant_text = text[15:60]
    palindromes = set()
    for length in range(16, 40):
        for i in range(len(relevant_text) - length + 1):
            substring = relevant_text[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes