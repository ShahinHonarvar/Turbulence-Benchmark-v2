def if_contains_anagrams(words):

    def normalize(s):
        return sorted(s.lower())

    def is_anagram(w1, w2):
        return normalize(w1) == normalize(w2)
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]) and len(words[i]) >= 3:
                count += 1
                if count >= 46:
                    return True
    return False