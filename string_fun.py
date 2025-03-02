word = "Python"
word_length = len(word) -1

def while_word_change(word, word_length):
    new_word = ""
    while word_length >= 0: 
        new_word = new_word + word[word_length]
        word_length = word_length-1
    
    print("while: " + new_word)
    
def for_range_word_change(word, word_length):
    new_word = ""
    for i in range(word_length+1):
        new_word = new_word + word[word_length]
        word_length = word_length - 1

    print("for: " + new_word)

while_word_change(word, word_length)
for_range_word_change(word, word_length)