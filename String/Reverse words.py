def reverse(sentence):
    words= sentence.split(' ')
    reverse_sentence= ' '.join(reversed(words))
    return reverse_sentence

sentence = input("Enter the sentence")
print(reverse(sentence))