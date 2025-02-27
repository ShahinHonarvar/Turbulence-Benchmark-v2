def palindromes_between_indices(s):
    letters = s[4:8]
    letters = letters.lower()
    unique_letters = set(letters)
    palindromes = set()
    n = len(letters)
    for i in range(1 << n):
        combination = ''
        for j in range(n):
            if i & 1 << j:
                combination += letters[j]
        if len(combination) >= 4:
            if combination == combination[::-1]:
                palindromes.add(combination)
    return palindromes