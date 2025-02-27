def palindromes_between_indices(s):
    s = s[3:8].lower()
    chars = 'abcdefghijklmnopqrstuvwxyz'
    result = set()
    for i in range(len(s), 5, -1):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring == substring[::-1]:
                result.add(substring)
    return result