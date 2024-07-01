def main():
    with open("books/frankestein.txt") as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
main()