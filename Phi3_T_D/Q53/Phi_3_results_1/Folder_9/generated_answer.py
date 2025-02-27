from itertools import combinations

def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    unique_letters = set(s)
    palindromes = set()
    for length in range(95, len(unique_letters) + 1):
        for combo in combinations(sorted(unique_letters), length):
            word = ''.join(combo)
            if len(word) < 95:
                continue
            for start in range(len(s) - len(word) + 1):
                segment = s[start:start + len(word)]
                if is_palindrome(segment):
                    palindromes.add(segment)
    return palindromes