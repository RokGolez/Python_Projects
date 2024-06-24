with open("story.txt","r") as f: # Context for the file
    story = f.read()

words = set() # Set instead of a list for distinct values
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story): # find all the words in the story
    if char == target_start:
        start_of_word = i
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i +1]
        words.add(word)
        start_of_word = -1

anwsers = {}

for word in words:
    anwser = input("Enter a word for " + word + ":")
    anwsers[word] = anwser

for word in words:
    story = story.replace(word,anwsers[word])  

print(story)




