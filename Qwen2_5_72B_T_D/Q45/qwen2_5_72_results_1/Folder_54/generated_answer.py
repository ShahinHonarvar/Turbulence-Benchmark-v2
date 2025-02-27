from itertools import permutations

def palindromes_between_indices(s):

    def generate_palindromes(chars):
        half_len = len(chars) // 2
        unique_chars = set(chars.lower())
        palindromes = set()
        for p in permutations(unique_chars, half_len):
            palindrome = ''.join(p) + (chars[len(chars) // 2].lower() if len(chars) % 2 else '') + ''.join(reversed(p))
            if len(palindrome) >= 4:
                palindromes.add(palindrome)
        return palindromes
    substring = s[4:10]
    return generate_palindromes(''.join((c for c in substring if c.isalpha())))