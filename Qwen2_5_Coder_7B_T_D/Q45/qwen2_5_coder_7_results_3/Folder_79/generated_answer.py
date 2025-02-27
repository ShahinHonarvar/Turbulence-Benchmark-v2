def palindromes_between_indices(s):
    letters = s[1:8].lower()
    letters = ''.join(filter(str.isalpha, letters))
    letters = ''.join(sorted(set(letters), key=letters.index))
    length = len(letters)
    if length < 3:
        return set()
    palindromes = set()
    for i in range(length - 1):
        for j in range(i + 2, length + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes