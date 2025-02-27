def is_palindrome(candidate):
    return candidate.lower() == candidate[::-1].lower()

def palindromes_between_indices(s):
    indices = range(5, 8)
    letters = ''.join(sorted(set((s[i] for i in indices)), key=s.index)).lower()
    length = len(letters)
    if length < 4:
        return set()
    palindromes = set()
    for start in range(length - 3):
        for end in range(start + 3, length + 1):
            candidate = letters[start:end]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes