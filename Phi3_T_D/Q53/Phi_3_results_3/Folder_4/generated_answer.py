from collections import defaultdict

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    letter_indices = defaultdict(list)
    for i, c in enumerate(s):
        if c.isalpha():
            letter_indices[c].append(i)
    palindromes = set()
    for letter, indices in letter_indices.items():
        for start in indices:
            for length in range(99, len(letters) + 1):
                substring = s[start:start + length]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes