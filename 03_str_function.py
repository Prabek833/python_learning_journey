name="prabek"
print(len(name))#len is the function that give length
print(name.startswith("pra"))
print(name.endswith("bek"))
print(name.capitalize())
print(name.upper())               # upper() converts all characters to uppercase
print(name.lower())               # lower() converts all characters to lowercase

print(name.isalpha())             # isalpha() checks if all characters are letters (no numbers or spaces)

print(name.replace("pra", "bra")) # replace(old, new) replaces part of string with another

print(name.find("be"))            # find() gives the index of substring, or -1 if not found

text = "  hello prabek  "
print(text)                       # original text with spaces
print(text.strip())               # strip() removes spaces from both ends

words = "I love Python".split()   # split() breaks string into list using space by default
print(words)                      # prints ['I', 'love', 'Python']

joined = "-".join(words)          # join() joins list elements into string with '-' between them
print(joined)                     # prints 'I-love-Python'

print(name.islower())             # islower() checks if all alphabetic characters are lowercase
print(name.isupper())             # isupper() checks if all alphabetic characters are uppercase

num_str = "12345"
print(num_str.isdigit())          # isdigit() checks if all characters are digits

mix_str = "prabek123"
print(mix_str.isalnum())          # isalnum() checks if all characters are letters or digits (no spaces)

multi_line = "hello\nworld"
print(multi_line)                 # \n is newline character, prints on two lines
print(multi_line.splitlines())    # splitlines() splits string at line breaks into a list

print(name[0])                    # indexing: gets first character of the string
print(name[-1])                   # negative index: gets last character of the string
print(name[1:4])                  # slicing: gets characters from index 1 to 3