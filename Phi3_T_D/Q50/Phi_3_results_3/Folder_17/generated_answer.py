def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        current_string = strings[i].lower()
        for j in range(i + 1, len(strings)):
            other_string = strings[j].lower()
            if len(current_string) >= 3 and len(other_string) >= 3 and (sorted(current_string) == sorted(other_string)):
                anagram_count += 1
                if anagram_count >= 97:
                    return True
    return False