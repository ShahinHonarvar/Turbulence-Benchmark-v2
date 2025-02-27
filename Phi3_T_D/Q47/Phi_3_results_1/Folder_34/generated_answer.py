def palindromes_of_specific_lengths(s):
    result = set()
    s = s[200:301].lower()
    for i in range(21, 81):
        for j in range(i + 9, min(i + 51, 101)):
            if s[i:j] == s[i:j][::-1]:
                result.add(s[i:j])
    return result