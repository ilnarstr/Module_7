
class WordFinder:
    res = {}
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        punctuation = ',.=!?;:'
        for file_name in self.file_names:
            words = []
            clear_line = ''
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    while line.find(' - ') != -1:
                        line = line.replace(' - ', ' ')
                        continue
                    for char in line:
                        if not char in punctuation:
                            clear_line += char
                words = clear_line.split()
            all_words[file_name] = words
            self.res.clear()
        return all_words

    def find(self, word):
        for names, words in self.get_all_words().items():
            place = 0
            if word.lower() in words:
                place = words.index(word.lower()) + 1
                self.res[names] = place
        return self.res

    def count(self, word):
        for names, words in self.get_all_words().items():
            counter = 0
            if word.lower() in words:
                counter = words.count(word.lower())
                self.res[names] = counter
        return self.res

finder2 = WordFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))