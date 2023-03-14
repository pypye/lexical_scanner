import re
class Scanner():
    def __init__(self, path):
        self.file_char = open(path, 'r', encoding='utf-8').read()
        self.count_char = 0
        self.remove_comment()

    def remove_comment(self):
        iniline_comment_pattern = re.compile(r'//.*')
        multiline_comment_pattern = re.compile(r'/\*.*?\*/', re.DOTALL)
        self.file_char = re.sub(iniline_comment_pattern, '', self.file_char)
        self.file_char = re.sub(multiline_comment_pattern, '', self.file_char)

    def peek_word(self):
        word = ""
        count_char = self.count_char

        while count_char < len(self.file_char):
            char = self.file_char[count_char]
            if char in [' ', '\t', '\n']: break
            count_char += 1
            word += char
        
        while count_char < len(self.file_char):
            char = self.file_char[count_char]
            if char not in [' ', '\t', '\n']: break
            count_char += 1
        return word
    
    def seek_word(self):
        while self.count_char < len(self.file_char):
            char = self.file_char[self.count_char]
            if char in [' ', '\t', '\n']: break
            self.count_char += 1
        return self.count_char < len(self.file_char)
    
    
    def peek_char(self):
        char = self.file_char[self.count_char]
        return char        

    def seek_char(self):
        self.count_char += 1 
        return self.count_char < len(self.file_char)
    
