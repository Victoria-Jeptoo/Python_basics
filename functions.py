#functions methods
from custom_function import greet
# opening  and writing to file
with open("temp.txt", "w") as file:
    file.write("99.34\n")
    file.write("100\n")
    file.write("54.34\n")
# opening and reading from file
with open("temp.txt", "r") as file:
    content = file.read()
    print(content)

# pip install yt-dlp
greet()

