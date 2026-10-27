# 08 - Count Vowels

st = str(input().lower())
vowel_count = 0
for letra in st:
    if letra in "aeiou":    
        vowel_count += 1
print(vowel_count)