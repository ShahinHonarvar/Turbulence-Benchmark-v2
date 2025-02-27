def palindromes_between_indices(text):
    letters = sorted(set(text.lower()[3:9]))
    result = set()

    def is_palindrome(s):
        return s == s[::-1]
    for x in letters:
        for y in letters:
            for z in letters:
                for w in letters:
                    for v in letters:
                        for u in letters:
                            word = x + y + z + w + v + u
                            if is_palindrome(word):
                                result.add(word)
    return result