def if_contains_anagrams(li):

    def char_list(s):
        s = s.lower()
        letters = [c for c in s if c.isalpha()]
        letters.sort()
        return ''.join(letters)
    combs = 0
    l = len(li)
    for i in range(l):
        for j in range(i + 1, l):
            if char_list(li[i]) == char_list(li[j]):
                combs += 1
                if combs > 44:
                    return False
    return True