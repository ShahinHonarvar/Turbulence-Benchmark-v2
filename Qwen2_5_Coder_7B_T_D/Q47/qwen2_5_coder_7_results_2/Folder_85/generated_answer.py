def palindromes_of_specific_lengths(s):
    result = set()
    substr = s[29:99].lower()
    for i in range(len(substr)):
        for j in range(i + 6, min(len(substr), i + 10) + 1):
            if substr[i:j] == substr[i:j][::-1] and substr[i:j].isalpha():
                result.add(substr[i:j])
    return result