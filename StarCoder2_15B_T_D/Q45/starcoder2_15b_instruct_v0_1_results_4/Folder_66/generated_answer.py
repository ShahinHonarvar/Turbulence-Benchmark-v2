from the English letters in `s` that occur between indices 0 and 5 (inclusive).

def palindromes_between_indices(s):
    """
    Finds all palindromes of length >= 5 in a given string `s` that can be formed
    """
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 5, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                palindromes.add(s[i:j + 1])
    return {p for p in palindromes if len(p) >= 5}