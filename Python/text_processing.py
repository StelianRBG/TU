import lorem

# Function to get number of lines of text and all words with 5 letters
def text_processing(text):
    lines = text.split('\n')
    print('Text is:\n' + text)
    print('===================================')
    print('Number of lines: ' + str(len(lines)))
    print('Words with 5 letters:')
    print([word for line in lines for word in line.replace('.', '').split() if len(word) == 5 ])

# Generate text
def generate_tex():
    n = int(input('Number of lines: '))
    return '\n'.join([lorem.sentence() for i in range(n)])

text_processing(generate_tex())
