print("Welcome to Language Translator")

language = input("Choose language (yoruba/igbo): ").lower()
word = input("Enter English word: ").lower()

if language == "yoruba":
    from languages.yoruba import translate
elif language == "igbo":
    from languages.igbo import translate
else:
    print("Language not supported")
    exit()

print("Translation:", translate(word))
