def palindromes_between_indices(s):
    filtered_chars = ''.join(filter(str.isalpha, s[1:5])).lower()
    length = len(filtered_chars)
    if length < 4:
        return set()
    palindromes = set()
    for i in range(length):
        for j in range(i + 4, length + 1):
            substring = filtered_chars[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes