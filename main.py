
def word_count(words):
    count = 0
    for i in words.split():
        count += 1

    return count

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(word_count(file_contents))
