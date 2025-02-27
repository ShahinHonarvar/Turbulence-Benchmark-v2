def palindromes_of_specific_lengths(s):
    s = s[2:9].lower()
    result = set()
    for i in range(len(s) - 2):
        for j in range(i + 3, i + 5):
            if j <= len(s):
                word = s[i:j]
                if word == word[::-1]:
                    result.add(word)
    return result