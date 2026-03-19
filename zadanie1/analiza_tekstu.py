import string

text = input("Podaj tekst: ")

chars_with_spaces = len(text)
chars_without_spaces = len(text.replace(" ", ""))

sentences = text.count(".") + text.count("!") + text.count("?")

clean_text = text.translate(str.maketrans("", "", string.punctuation))
clean_text = clean_text.lower()

words = clean_text.split()

word_count = len(words)

longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

max_count = max(word_freq.values())

most_common = []
for word, count in word_freq.items():
    if count == max_count:
        most_common.append(word)

print("Statystyki tekstu:")
print("Liczba znaków (ze spacjami):", chars_with_spaces)
print("Liczba znaków (bez spacji):", chars_without_spaces)
print("Liczba słów:", word_count)
print("Liczba zdań:", sentences)
print("Najdłuższe słowo:", longest_word)
print("Najczęstsze słowo:", ", ".join(most_common))