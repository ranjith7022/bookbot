def word_count(text):
    return len(text.split())

def char_count(text):
    count = {}
    text = text.lower()
    for i in text:
        if i in count:
            count[i]+=1
        else:
            count[i] = 1
    return count


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    wc = word_count(file_contents)
    cc = char_count(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wc} words found in the document")
    print()
    for item,count in cc.items():
        print(f"The \'{item}\' character was found {count} times")
    print("--- End report ---")












if __name__ == "__main__":
    main()
