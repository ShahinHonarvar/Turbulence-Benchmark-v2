def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3 and (len(s2) >= 3)
    count = 0
    words = sorted(words, key=lambda x: sorted(x.lower()))
    i, j = (0, 1)
    while i < len(words) and j < len(words):
        if is_anagram(words[i], words[j]):
            count += 1
            j += 1
            if j == len(words):
                break
        elif words[i].lower() < words[j].lower():
            i += 1
            j = max(i + 1, j)
        else:
            j += 1
    return count >= 246