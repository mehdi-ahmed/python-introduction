message = input("> ")
words = message.split(' ')   # returns an array of word according to the splitter ' '

emojis = {
    ":)": "😊",
    ":(": "😒"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)
