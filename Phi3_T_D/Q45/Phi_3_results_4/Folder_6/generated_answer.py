def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    letters_set = set(s.lower()[0:8])
    palindromes = set()
    for length in range(4, min(8, len(letters_set) + 1) + 1):
        if length % 2 == 0:
            for h in letters_set:
                for k in letters_set - {h}:
                    if is_palindrome(h + k + k + h):
                        palindromes.add(h + k + k + h)
        else:
            for h in letters_set:
                if any((is_palindrome(h + j + j + h) for j in letters_set - {h})):
                    palindromes.add(h + j + j + h)
    return palindromes