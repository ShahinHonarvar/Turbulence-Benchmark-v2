def palindromes_between_indices(s):
    sub_str = s[4:10]
    letters = ''.join(sorted(filter(str.isalpha, sub_str.lower())))
    palindromes = set()
    if len(letters) < 5:
        return palindromes
    for i in range(len(letters) - 4):
        center = letters[i:i + 5]
        if center == center[::-1]:
            palindromes.add(center)
    return palindromes