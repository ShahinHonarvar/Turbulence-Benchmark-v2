def palindromes_between_indices(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = s[:9].lower()
    letters = sorted(s)
    n = len(letters)
    result = set()

    def permute(data, m=len(letters)):
        if m == 0:
            result.add(''.join(data))
        for i in range(m):
            permute(data[:i] + data[i + 1:], m - 1)
    permute(letters)
    for word in result:
        if len(word) >= 7 and is_palindrome(word):
            result.add(word)
    return result