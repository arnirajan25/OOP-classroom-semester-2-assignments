with open("practice.txt", "w") as f:
    f.write("Hi everyone\n")
    f.write("we are learning File I/O\n")
    f.write("using Java.\n")
    f.write("I like programming in Java.\n")

with open("practice.txt", "r") as f:
    content = f.read()

print(content)

content = content.replace("Java", "Python").replace("java", "python")
-----------------------------------------------------------------------
with open("practice.txt", "w") as f:
    f.write(content)

print("File updated:")
print(content)
def checkforword():

    with open("practice.txt", "r") as f:
        content = f.read()

        if "learning" in content:
            print("The word 'learning' exists in the file.")
        else:
            print("The word 'learning' does NOT exist in the file.")
-----------------------------------------------------------------------
with open("practice.txt", "r") as f:
    data = f.readlines()
    print(data)
    
def find_line_with_word(filename, word):
    with open(filename, "r") as f:
        for line_num, line in enumerate(f, start=1):
            if word in line:
                return line_num
    return -1

result = find_line_with_word("practice.txt", "learning")
print(result)
-----------------------------------------------------------------------
def count_even_numbers(filename):
    with open(filename, "r") as f:
        data = f.read()

    numbers = data.split(",")
    count = 0

    for num in numbers:
        num = num.strip()  
        if num.isdigit() or (num.startswith('-') and num[1:].isdigit()):
            if int(num) % 2 == 0:
                count += 1

    return count

result = count_even_numbers("numbers.txt")
print("Count of even numbers:", result)
