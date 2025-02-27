from itertools import combinations

def palindromes_of_specific_lengths(s: str):

    def is_palindrome(chars: str) -> bool:
        return chars.lower() == chars.lower()[::-1]
    valid_range = (124, 283)
    palindromes = set()
    substring = s[valid_range[0]:valid_range[1] + 1]
    for length in range(115, 135):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if all((c.isalpha() for c in candidate)):
                if is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes