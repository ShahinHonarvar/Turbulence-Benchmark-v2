def palindromes_between_indices(text):
    start_index, end_index = (8, 9)
    substrings = set()
    for char in text[start_index:end_index + 1]:
        if char.isalpha():
            substrings.add(char.lower())
    palindromes = set()
    for i in range(len(substrings)):
        for j in range(i, len(substrings)):
            substring = ''.join(sorted(substrings)[i:j + 1])
            if len(substring) >= 3 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes