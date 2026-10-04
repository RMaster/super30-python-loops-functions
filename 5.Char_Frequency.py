# Q5: Character Frequency Counter
# Why a for loop? We must look at every character in the string once,
# so "for ch in text" is the natural choice.
# Why a dictionary? It stores a count against each character (key -> value).

text = input("Enter a string: ")

if len(text) == 0:
    print("The string is empty, so there is nothing to count.")
    exit()

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(f"\nCharacter frequencies in '{text}':")
for ch in freq:
    print(f"'{ch}' : {freq[ch]}")