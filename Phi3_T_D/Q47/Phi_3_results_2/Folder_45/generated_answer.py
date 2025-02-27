def palindromes_of_specific_lengths(s):
    s = s[70:141]
    palindromes = set()

    def expand(center1, center2):
        left, right = (center1, center2)
        total_characters = right - left + 1
        while left >= 0 and right < len(s) and (total_characters <= 60):
            if s[left].isalpha() and s[right].isalpha():
                if s[left].lower() == s[right].lower():
                    palindromes.add(s[left:right + 1])
                    left -= 1
                    right += 1
                    total_characters += 1
                else:
                    break
            else:
                break
    for i in range(len(s) - 2):
        if s[i].isalpha():
            expand(i, i)
            if i + 1 < len(s) and s[i + 1].isalpha():
                expand(i, i + 1)
    return palindromes