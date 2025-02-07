def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

user_input = input("Введите предложение: ")
result = reverse_words(user_input)
print(result)