from search_text import search_and_replace_text

text = "The text I need to edit, I made it so it replaces the dot so the second sentence won't start from a dot."

sentence = str(input("the two words that are next to each other from the text you want to move to the end: "))

text = search_and_replace_text(sentence, text)

print(text)
