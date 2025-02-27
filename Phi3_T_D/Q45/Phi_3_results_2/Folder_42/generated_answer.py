import itertools

def palindromes_between_indices(s):
    substr = s[6:10].lower()
    chars = set(substr)
    if len(chars) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(substr) + 1):
        for combo in itertools.combinations_with_replacement(chars, length):
            mid = '' if length % 2 == 0 else chars
            palindrome_part = ''.join(sorted(list(combo) + list(mid)))
            for i in range(len(palindrome_part) // 2):
                l, r = (i, len(palindrome_part) - 1 - i)
                if palindrome_part[l] != palindrome_part[r]:
                    break
            else:
                palindromes.add(palindrome_part)
    return palindromes