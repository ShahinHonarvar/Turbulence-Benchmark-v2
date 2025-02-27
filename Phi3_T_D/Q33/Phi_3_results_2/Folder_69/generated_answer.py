def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [ch for ch in s[641:872] if is_between(ch, '>', 'q') and ch in vowels]

def is_between(char, char1, char2):
    char_range = '! " # $ % & \' ( ) * + , - . / :;< = > ? @ [\\] ^ _ ` { | } ~'
    return char_range.index(char1) < char_range.index(char) < char_range.index(char2)