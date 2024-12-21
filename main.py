
def word_count(words):
    count = 0
    for i in words.split():
        count += 1

    return count

def char_count(words):
    char_counts = []
    for char in words.lower():
        if not char.isalpha():
            continue
            
        if len(char_counts) == 0:
            char_counts.append({"character": char, "count": 1})
        else:
            found = False
            for i in char_counts:
                if i["character"] == char:
                    i["count"] += 1
                    found = True
            
            if not found:
                char_counts.append({"character": char, "count": 1})

    return char_counts

file_path = "books/frankenstein.txt"
with open(file_path) as f:
    file_contents = f.read()
    words = word_count(file_contents)
    chars = char_count(file_contents)

    print(f"--- Begin report of {file_path} ---")
    print(f"{words} words found in the document")
    print("")

    chars = sorted(chars, reverse=True, key=lambda a: a["count"])

    for char in chars:
        print(f"The '{char['character']}' character was found {char['count']} times")

    print("--- End report ---")

