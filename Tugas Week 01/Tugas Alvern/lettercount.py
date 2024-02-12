Word = "lettercount"
Devider = dict()
for letter in Word:
    if letter in Devider:
        Devider[letter] += 1
    else:
        Devider[letter] = 1

print("Jumlah Huruf:")
for letter, count in Devider.items():
    print(f"{letter}: {count}")