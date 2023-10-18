import os
cwd = os.getcwd()
path = os.path.join(cwd, "python","part_I", "test.txt")
print(path)
#open file and write content
try:
    with open(path, 'w') as file:
        file.write("Hello World!")
        #close file
        file.close()
except FileNotFoundError:
    print("Dosya bulunamadı.")
except Exception as e:
    print("Bir hata oluştu:", e)

#open file and read content

try:
    with open(path, 'r') as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("Dosya bulunamadı.")
except Exception as e:
    print("Bir hata oluştu:", e)


#open file and append content

try:
    with open(path, 'a') as file:
        file.write("\nHello World Again!")
except FileNotFoundError:
    print("Dosya bulunamadı.")
except Exception as e:
    print("Bir hata oluştu:", e)