def palindromes_of_specific_lengths(s):
    s = s[63:71].lower()
    result = set()
    for i in range(len(s) - 3):
        for j in range(i + 4, i + 6):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result