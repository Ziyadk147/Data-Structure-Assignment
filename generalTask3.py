
def count_words_in_poem(file_path):
    word_count = {}  
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip().lower()  
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count

word_count = count_words_in_poem('poem.txt')

print(f"Word count for 'diverged': {word_count.get('diverged', 0)}")
print(f"Word count for 'in': {word_count.get('in', 0)}")
print(f"Word count for 'i': {word_count.get('i', 0)}")