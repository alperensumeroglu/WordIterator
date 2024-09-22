'''
WordIterator Project
The WordIterator project is a custom Python iterator designed to iterate over the characters of a given word. It allows users to specify a starting index from which the iteration begins, making it flexible for different use cases. The iterator handles invalid input gracefully and ensures that users can easily explore and access the characters of any word they choose.
Features:
Accepts user input for both the word and the starting index.
Implements the iterator protocol with __iter__() and __next__() methods.
Provides validation for the starting index to prevent out-of-bounds errors.
This project serves as a practical example of how to create and use iterators in Python, enhancing understanding of the iterator design pattern and object-oriented programming principles.
'''
class WordIterator:
    def __init__(self, word, index):
        self.word = word # Get the word
        self.index = index # Set the starting index
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.word):
            letter = self.word[self.index]
            self.index += 1
            return letter
        else:
            raise StopIteration
def get_valid_integer(prompt, max_value):
    while True:
        try:
          value = int(input(prompt))
          if 0 <= value < max_value:
              return value
        except ValueError:
           print('Invalid input. Please enter a integer.')
user_word = input('Enter a word: ')
start_index = get_valid_integer(f'At which character index would you like to start? (0 to {len(user_word) - 1}: ', len(user_word))
my_word = WordIterator(user_word, start_index)
for letter in my_word:
   print(letter)
