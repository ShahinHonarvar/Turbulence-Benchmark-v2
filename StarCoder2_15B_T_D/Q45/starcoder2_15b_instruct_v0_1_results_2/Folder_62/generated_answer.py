def palindromes_between_indices(text):
    count = [0] * 26
    for c in text:
        if 'a' <= c <= 'z':
            count[ord(c) - ord('a')] += 1
    palindromes = set()
    for i in range(26):
        if count[i] >= 7:
            palindromes.add(chr(i + ord('a')) * 7)
    return palindromes