def palindromes_between_indices(s):
    chunk = s[4:9].lower()
    letters = ''.join(sorted(chunk))
    seen = set()

    def generate_palindromes(s, left, right):
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            left -= 1
            right += 1
        for i in range(left + 2, right):
            for j in range(i, right):
                sub = s[i:j + 1]
                if len(sub) >= 3 and sub == sub[::-1]:
                    seen.add(sub)
            left = i
            right = j
    generate_palindromes(letters, 0, 0)
    return seen