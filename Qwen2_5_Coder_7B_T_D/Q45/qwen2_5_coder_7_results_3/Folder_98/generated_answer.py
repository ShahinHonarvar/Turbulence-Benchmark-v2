def palindromes_between_indices(s):
    target = s[3:6].lower()
    target_chars = set(target)
    result = set()

    def is_palindrome(word):
        return word == word[::-1]
    for i in range(len(target_chars)):
        for j in range(i, len(target_chars)):
            for k in range(j, len(target_chars)):
                for l in range(k, len(target_chars)):
                    word = ''.join(target_chars[i]) * 4 + ''.join(target_chars[j]) * 4 + ''.join(target_chars[k]) * 4 + ''.join(target_chars[l]) * 4
                    if is_palindrome(word) and len(word) >= 4:
                        result.add(word)
    return result