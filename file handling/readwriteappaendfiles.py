def write(textfile, text):
    try:
        with open(textfile, 'w') as file:
            file.write(text)
        print(f"Text written to {textfile} successfully.")
    except Exception as e:
        print(f"An error occurred while writing to {textfile}: {e}")

#write('test.txt', 'Hello, World! amar')

def read(textfile):
    try:
        with open(textfile, 'r') as file:
            content = file.read()
        print(f"Content of {textfile}:")
        print(content)
    except FileNotFoundError:
        print(f"The file {textfile} does not exist.")
    except Exception as e:
        print(f"An error occurred while reading {textfile}: {e}")
    
#read('test.txt')

def a():
    f = open('song.txt', 'r')
    data = f.read()
    print(data)
    f.close() # read the file

def length():
    f = open('song.txt', 'r')
    data = f.read()
    print("there are ", len(data), "characters in the file")
    f.close()

def t():
    f = open('song.txt', 'r')
    data = f.readlines()
    count = 0
    for line in data:
        count += 1 #counting the number of lines
    print("Number of lines:", count) 
    print(data)
    f.close()

def uppercasecheck():
    f = open('song.txt', 'r')
    data = f.read()
    if data.isupper(): # check if the string is uppercase
        print("The file is in uppercase.")
    else:
        print("The file is not in uppercase.")
    f.close()

def lowercheck():
    f = open('song.txt', 'r')
    data = f.read()
    countcharacter = 0
    for line in data:
        if line.islower():
            countcharacter += 1
    print("Number of characters in lowercase:", countcharacter)   
       
if __name__ == '__main__':
    # Uncomment one of the following lines to execute a function
    #write('test.txt', 'Hello, World! amar')
    #read('test.txt')
    #a()
    #length()
    #t()
    uppercasecheck()
    lowercheck()