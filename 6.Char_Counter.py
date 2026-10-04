# Q6: Vowel, Consonant, Digit, Space and Special Character Counter
# Why a for loop? We must examine every character of the sentence once,
# so "for ch in sentence" is the natural choice.

sentence = input("Enter a sentence: ")

if len(sentence) == 0:
    print("The sentence is empty, so there is nothing to count.")
    exit()

vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in sentence:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

print(f"\nSentence: {sentence}")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Special characters: {special}")