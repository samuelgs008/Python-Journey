# 08 - Count Vowels
st = str(input().lower().replace(" ", ""))
vowel_count = 0
consonant_count = 0
for letra in st:  
    vowel_count += letra in "aeiou"
    consonant_count = len(st) - vowel_count
print(f"VOWELS = {vowel_count}")
print(f"CONSONANTS = {consonant_count}")