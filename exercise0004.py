def count_word(filename):
    with open(filename,encoding = 'utf-8') as f:
        contents = f.read()
    words = contents.split()
    num_word = len(words)
    print(f"The file {filename} has about {num_word} words.")
    
if __name__ == "__main__":
    count_word('little_women.txt')