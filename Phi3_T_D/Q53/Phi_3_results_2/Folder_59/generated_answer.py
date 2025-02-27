def palindrome_of_length_at_least_n(s):

    def find_palindromes(s, left, right):
        stack = [(left, right)]
        palindromes = set()
        while stack:
            start, end = stack.pop()
            if end - start + 1 >= 20 and s[start:end + 1].lower() == s[start:end + 1][::-1]:
                palindromes.add(s[start:end + 1])
            for i in range(start, right + 1):
                if s[start].lower() == s[i].lower() and i + 1 <= end:
                    if s[start:i + 1].lower() == s[start:i + 1][::-1]:
                        stack.append((start, i))
                    stack.append((i + 1, right))
        return palindromes
    left, right = (0, len(s) - 1)
    return find_palindromes(s, left, right)