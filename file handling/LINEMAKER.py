def write(textfile, text):
    try:
        with open(textfile, 'w') as file:
            file.write(text)
        print(f"Text written to {textfile} successfully.")
    except Exception as e:
        print(f"An error occurred while writing to {textfile}: {e}")

write("sectest.txt", "fibbonacci numbers\npalindromic numbers\npi\ncube roots\nlinear functions\nvelocity formulae\nmeters\n60 seconds\nphysics\narithmetics")