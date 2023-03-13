class Scanner():
    def __init__(self, path):
        self.file_char = open(path, 'r', encoding='utf-8')
        self.file_word = open(path, 'r', encoding='utf-8')
        self.count_char = 0
        self.count_word = 0
    
    def peek_word(self):
        word = ""
        while True:
            char = self.file_word.read(1)
            self.count_word += 1
            if char in [' ', '\t', '\n']: break
            word += char
        
        while True:
            char = self.file_word.read(1)
            self.count_word += 1
            if char not in [' ', '\t', '\n']: break

        self.count_word -= 1
        self.file_word.seek(self.count_word)
        return word
    
    
    def peek_char(self):
        char = self.file_char.read(1)
        self.count_char += 1
        return char                 
    
    def seek_char_to_current_word(self):
        self.file_char.seek(self.count_word)
        self.count_char = self.count_word