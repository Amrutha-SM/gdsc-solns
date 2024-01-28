#Problem 3

def is_palindrome(word):
    return word == word[::-1]

def result(sentence):
    words = sentence.split()
    result = []

    for word in words:
        if not is_palindrome(word):
            l=len(word)
            palindrome_word = word + word[l-2::-1]
            result.append(palindrome_word)
        else:
            result.append(word)

    return ' '.join(result)

insentence = input("Enter a sentence: ")
outsentence = result(insentence)

print("\nChanged Sentence:")
print(outsentence)
