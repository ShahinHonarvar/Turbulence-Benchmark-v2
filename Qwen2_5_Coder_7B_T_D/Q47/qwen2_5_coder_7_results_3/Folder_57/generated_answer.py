def palindromes_of_specific_lengths(s):
    s = s[16:95].lower()
    words = s.split()
    result = set()
    for word in words:
        if len(word) >= 39 and len(word) <= 52 and (word == word[::-1]):
            result.add(word)
    return result