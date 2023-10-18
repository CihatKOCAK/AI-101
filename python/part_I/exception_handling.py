try:
    1 / 0
except:
    print("You cannot divide by zero!")


my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except IndexError:
    print("This index does not exist!")
except KeyError:
    print("This key is not in the dictionary!")
except:
    print("Some other error occurred!")

    
try:
    num1 = int(input("Bölünen sayıyı girin:"))
    num2 = int(input("Bölen sayıyı girin: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Sıfıra bölme hatası! Bölen sıfır olamaz.")
except ValueError:
    print("Geçersiz giriş! Lütfen geçerli bir sayı girin.")
except Exception as e:
    print("Bir hata oluştu:", e)
else:
    print(f"Sonuç: {result}")
finally:
    print("İşlem tamamlandı.")
