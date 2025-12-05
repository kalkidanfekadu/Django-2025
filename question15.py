sentence=input("enter sentence")
word_count = {}
word = ""  
for char in sentence:
    if char != " ":  
        word += char
    else:
        if word:  
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
            word = ""  
if word:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)