def is_palindrome(word):
    cleaned = ''.join(filter(str.isalnum, word)).lower()
    return cleaned == cleaned[::-1]

print(is_palindrome("мадам")) 
print(is_palindrome("hello"))