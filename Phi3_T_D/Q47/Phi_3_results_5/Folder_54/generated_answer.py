def is_english_letter(ch):
    return 'a' <= ch <= 'z'

def find_palindromes_of_specific_lengths(s):
    palindromes = set()
    for start in range(27, min(78, len(s) - 17)):
        for length in range(18, 20):
            substring = s[start:start + length].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes