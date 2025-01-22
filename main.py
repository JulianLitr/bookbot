print("hello world")
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        words = file_contents.split()
        lowered_words = [word.lower() for word in words]
        #print(lowered_words)
        char_count = {}
        for word in lowered_words:
            for letter in word:
                if letter in char_count:
                    char_count[letter] += 1
                else:
                    char_count[letter] = 1
        # Include spaces in char_count
        spaces_count = file_contents.count(' ')
        if ' ' in char_count:
            char_count[' '] += spaces_count
        else:
            char_count[' '] = spaces_count
        #print(char_count)
        onlyalpha = {k: v for k, v in char_count.items() if k.isalpha()}
        order = sorted(onlyalpha)
        for i in order:
            print(f"The '{i}' was found {char_count[i]} times.")

main()