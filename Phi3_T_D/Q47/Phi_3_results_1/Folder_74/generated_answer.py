def is_palindrome(s: str, case_insensitive: bool=False) -> bool:
    if case_insensitive:
        s = s.lower()
    return s == s[::-1] and s.isalpha()

def palindromes_of_specific_lengths(text: str) -> set:
    substring = text[30:85]
    return set((substring[i:j] for i in range(len(substring)) for j in range(i + 12, min(i + 21, len(substring) + 1)) if is_palindrome(substring[i:j])))