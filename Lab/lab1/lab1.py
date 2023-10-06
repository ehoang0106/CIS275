
def count_vowels(string_input):
    string_input = string_input.lower()
    vowel_counts = [0,0,0,0,0]

    for char in string_input:
        if char == 'a':
            vowel_counts[0] += 1
        elif char == 'e':
            vowel_counts[1] += 1
        elif char == 'i':
            vowel_counts[2] += 1
        elif char == 'o':
            vowel_counts[3] += 1
        elif char == 'u':
            vowel_counts[4] += 1

    return vowel_counts

def main():
    enterString = input("Enter string: ")
    vowel_counts = count_vowels(enterString)

    vowels = ['A', 'E', 'I', 'O', 'U']

    for i in range(len(vowels)):
        print(f'{vowels[i]} : {vowel_counts[i]}')

main()