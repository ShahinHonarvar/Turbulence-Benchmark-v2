def palindrome_of_length_at_least_n(s):
    s = s.lower()

    def find_palindromes(sub_s):
        left, right = (0, len(sub_s) - 1)
        while right > left:
            if sub_s[left] != sub_s[right]:
                break
            left += 1
            right -= 1
        return (left, right)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 57, len(s) + 1):
            left, right = find_palindromes(s[i:j])
            if right < j:
                continue
            palindrome = s[left:right + 1]
            if len(palindrome) >= 57:
                palindromes.add(palindrome)
    return palindromes