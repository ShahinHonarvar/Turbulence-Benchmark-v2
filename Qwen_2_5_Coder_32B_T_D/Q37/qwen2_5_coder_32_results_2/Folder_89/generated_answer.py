def filter_chars(s):
    chars_to_remove = set(s[11:33]) & set('! " # $ % & \' ( ) * + , - . / : ; < = > ? @')
    return ''.join((c for c in s if c not in chars_to_remove))