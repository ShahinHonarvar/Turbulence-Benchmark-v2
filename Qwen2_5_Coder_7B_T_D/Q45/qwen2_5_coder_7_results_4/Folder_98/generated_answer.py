def palindromes_between_indices(s):
    chars = s[3:6].lower()
    chars = ''.join(sorted(set(chars)))
    length = len(chars)
    if length < 4:
        return set()
    palindromes = set()
    for i in range(length - 3 + 1):
        for j in range(i + 3, length + 1):
            word = chars[i:j]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes