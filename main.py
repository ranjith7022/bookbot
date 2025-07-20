import sys
from stats import word_count, char_count, sort_on


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        with open(f"{sys.argv[1]}", encoding="utf-8", errors="ignore") as f:
            file_contents = f.read()
        wc = word_count(file_contents)
        cc = char_count(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"Found {wc} total words")
        print()
        new_cc = sort_on(list(cc.items()))
        for item, count in new_cc:
            if item.isalpha():
                print(f"{item}: {count}")
        print("--- End report ---")


if __name__ == "__main__":
    main()
