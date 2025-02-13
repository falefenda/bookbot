def main():
    book_dictionary = {}
    alpha_count = {}

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    lc_file_contents = file_contents.lower()
    for char in lc_file_contents:
        if char in book_dictionary:
            book_dictionary[char]+=1
        else:
            book_dictionary[char] = 1

    for key, value in book_dictionary.items():
        if key.isalpha():
            alpha_count[key] = value

    alpha_count_list = sorted(alpha_count.items(), key=lambda x:x[1], reverse=True)
    
    for letter in alpha_count_list:
        print(f"The '{letter[0]}' character was found {letter[1]} times")



main()