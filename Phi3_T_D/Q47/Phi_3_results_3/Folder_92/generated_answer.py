def palindromes_of_specific_lengths(s):
    substr = s[:5]
    substr = ''.join(filter(str.isalpha, substr)).lower()
    return {substr[i:j + 1] for i in range(len(substr)) for j in range(i, min(i + 4, len(substr))) if i + j + 1 >= 3 and i + j + 1 <= 4 and (substr[i:j + 1] == substr[i:j + 1][::-1])}