def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def palindromes_between_indices(s):
    palindromes = set()
    for i in range(1, 6):
        for j in range(i + 4, 6):
            substr = s[i - 1:j].lower()
            if len(substr) >= 4 and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes