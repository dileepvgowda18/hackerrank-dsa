def count_vowels(s):
    count = 0

    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1

    return count

print(count_vowels("education"))
