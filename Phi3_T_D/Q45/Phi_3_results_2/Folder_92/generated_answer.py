from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[3:8]
    english_letters = sorted(filter(str.isalpha, substring.lower()))
    if len(english_letters) < 4:
        return set()

    def generate_palindromes(chars):
        if len(chars) < 4:
            return
        for i in range(len(chars)):
            current = chars[i]
            for p in permutations(chars[:i] + chars[i + 1:]):
                candidate = current + ''.join(p) + current
                if is_palindrome(candidate):
                    yield candidate
    return set(generate_palindromes(english_letters))