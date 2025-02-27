def palindromes_of_specific_lengths(s):
    substr = s[124:284].lower()
    result = set()
    for i in range(len(substr)):
        for j in range(i + 115, min(i + 135, len(substr) + 1)):
            if substr[i:j] == substr[i:j][::-1] and substr[i:j].isalpha():
                result.add(substr[i:j])
    return result