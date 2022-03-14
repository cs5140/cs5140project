words  = []
while i < len(text):
    index = text.find("<a ")
    text = text[index:]
    index = text.find(">")
    text = text[index:]
    index = text.find("</a")
    word = text[:index]
    word = word.replace(">","")
    word = word[:word.find(", ")]
    words.append(word)
    text = text[index:]
    i+=1
print(words)