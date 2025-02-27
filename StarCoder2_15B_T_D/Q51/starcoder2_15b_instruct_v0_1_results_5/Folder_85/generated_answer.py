def if_contains_anagrams(strings):
    anagram_pairs = 0
    char_counts = [0] * 26
    for s in strings:
        if len(s) >= 3:
            s = s.lower()
            char_counts = [0] * 26
            for c in s:
                if 97 <= ord(c) <= 122:
                    char_counts[ord(c) - 97] += 1
            for i in range(len(strings)):
                if i != strings.index(s) and len(strings[i]) >= 3:
                    other_s = strings[i].lower()
                    other_char_counts = [0] * 26
                    for c in other_s:
                        if 97 <= ord(c) <= 122:
                            other_char_counts[ord(c) - 97] += 1
                    if char_counts == other_char_counts:
                        anagram_pairs += 1
    return anagram_pairs <= 276