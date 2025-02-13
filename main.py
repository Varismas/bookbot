def main():
    with open("/home/varismas/workspace/github.com/Varismas/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        word_total = word_count(file_contents)
        char_count = letter_count(file_contents)
        
        # Create the list of dictionaries here
        letters = []
        for char in char_count:
            if char.isalpha():
                char_dict = {"char": char, "num": char_count[char]}
                letters.append(char_dict)
        
        # Sort the list
        letters.sort(reverse=True, key=sort_on)
        
        # Print the report
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_total} words found in the document\n")
        
        # Print each character count
        for item in letters:
            print(f"The '{item['char']}' character was found {item['num']} times")
        
        print("--- End report ---")
def sort_on(dict):
    return dict["num"]

def word_count(text):
    words = text.split()
    total_words= len(words)
    return total_words


def letter_count (text):
    lowered_text = text.lower()
    char_count = {}
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

if __name__ == "__main__":
    main ()