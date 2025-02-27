def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def unique_english_letters(s: str) -> str:
    return ''.join(sorted(set(filter(str.isalpha, s.lower()))))

def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[23:83]
    palindromes = set()
    for start in range(len(substring) - 33):
        for end in range(start + 31, start + 34 + 1):
            if end <= len(substring):
                segment = unique_english_letters(substring[start:end])
                if is_palindrome(segment):
                    palindromes.add(segment)
    return palindromes