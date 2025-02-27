def palindromes_of_specific_lengths(s):
    substr = s[18:99].lower()
    result = set()
    for i in range(len(substr)):
        for j in range(i + 31, min(i + 52, len(substr) + 1)):
            if substr[i:j] == substr[i:j][::-1]:
                result.add(substr[i:j])
    return result