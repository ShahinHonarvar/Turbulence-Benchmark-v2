def palindromes_of_specific_lengths(s):

    def expand_around_center(left, right):
        while left >= 10 and right <= 100 and (right - left + 1 >= 10 and right - left + 1 <= 50):
            if s[left:right + 1].lower() == s[left:right + 1][::-1].lower():
                yield s[left:right + 1]
            left -= 1
            right += 1
    return set((palindrome for center in range(10, 101) for palindrome in expand_around_center(center, center)))