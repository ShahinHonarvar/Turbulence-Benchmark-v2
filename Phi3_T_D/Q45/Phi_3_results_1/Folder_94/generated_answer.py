from itertools import permutations

def is_palindrome(s: str) -> bool:
    return s.lower() == s[::-1].lower()

def palindromes_between_indices(s: str) -> set:
    result = set()
    middle_chars = s[3:5]
    chars = set(middle_chars.lower())
    if len(chars) < 3:
        return result
    for length in range(3, len(chars) + 1):
        for perm in permutations(chars, length):
            candidate = ''.join(perm)
            if length == 3:
                result.add(candidate)
            else:
                for i in range(1, length - 1):
                    result.add(candidate[:i] + candidate[i] + candidate[i - 1] + candidate[i + 1:])
    return result