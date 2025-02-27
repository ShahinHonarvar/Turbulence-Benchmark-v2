def palindrome_of_length_at_least_n(s):
    s = s.lower()

    def is_palindrome(word):
        return word == word[::-1]

    def find_palindromes(seg, lo, hi):
        if hi <= lo:
            return []
        results = []
        for i in range(lo, hi):
            wing_left, wing_right = (1, 0)
            while lo - wing_left >= 0 and hi + wing_right < len(seg) and (seg[lo - wing_left] == seg[hi + wing_right]):
                wing_left += 1
                wing_right += 1
            center_mirrored = [[lo - wing_left + 1, hi + wing_right]]
            j = lo - wing_left
            k = hi + wing_right
            while j >= 0 and k < len(seg) and (seg[j] == seg[k]):
                j -= 1
                k += 1
            center_mirrored.append([j + 1, k - 1])
            results += center_mirrored
        return results
    results = []
    for center in range(len(s)):
        left, right = find_palindromes(s, center, center)
        results += left + right
    return {s[lo:hi + 1] for lo, hi in results if hi + 1 - lo >= 27}