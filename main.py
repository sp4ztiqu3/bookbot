
def word_count(words):
    count = 0
    for i in words.split():
        count += 1

    return count

def char_count(words):
    char_counts = {}
    for char in words.lower():
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    return char_counts

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(word_count(file_contents))
    print(char_count(file_contents))
