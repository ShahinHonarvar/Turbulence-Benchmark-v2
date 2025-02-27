def palindromes_between_indices(s):
    substring = s[2:9].lower()
    length = len(substring)
    if length < 6:
        return set()
    letters = list(substring)
    unique_letters = set(substring)
    palindromes = set()
    for i in range(length):
        for j in range(i + 6, length + 1):
            substring = ''.join(sorted(letters[i:j]))
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes