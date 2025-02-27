def palindromes_of_specific_lengths(s):
    s = s[124:284]
    result = set()
    for length in range(115, 135):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                result.add(s[i:i + length])
    return result