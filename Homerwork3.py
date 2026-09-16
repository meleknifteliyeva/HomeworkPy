"""
Dərs 5 — Ev tapşırığı
Mövzular:
- Conditional Statements və Loops — əlavə mövzular
- Strings ilə işləmə

Qaydalar:
- Bütün tapşırıqları bu faylın içində həll edin.
- Tapşırıq şərhlərini silməyin.
- Hər tapşırığın kodunu uyğun hissənin altına yazın.
- Proqramı fərqli input-larla test edin.
- Hazır kodu internetdən copy-paste etməyin.
- Məqsəd syntax-ı əzbərləmək yox, məntiqi özünüz qurmaqdır.
"""

# ============================================================
# TAPŞIRIQ 1 — Username yoxlanışı
# ============================================================

# İstifadəçidən username alın.
# Qaydalar:
# - əvvəl və sondakı boşluqlar silinsin
# - minimum 5 character olsun
# - username daxilində space olmasın
#
# Uyğundursa:
# Username accepted
#
# İPUCU:
# strip(), len(), " " in username, if / elif / else

# Kodunuzu burada yazın:
"""
username = input("Please enter your username: ")
while(True):
    username = username.strip()
    if(len(username) < 5):
        print("Username must be at least 5 character long")
        username = input("Please enter your username: ")
    else:
        if (" " in username ):
            print("There shouldn't be any spaces in the username")
            username = input("Please enter your username: ")
        else:
            print("Username accepted")
            break
""" 

# ============================================================
# TAPŞIRIQ 2 — Mətn analizi
# ============================================================

# İstifadəçidən bir text alın.
# Çap edin:
# - ümumi uzunluq
# - ilk character
# - son character
# - böyük hərflərlə forması
# - kiçik hərflərlə forması
#
# İPUCU:
# len(), indexing, negative indexing, upper(), lower()

# Kodunuzu burada yazın:
"""
text = input("Please enter your text: ")
Length = len(text)
print("Length of your text: ", Length)
first_character = text[0]
print("First chracter of your text: ",first_character)
last_character = text[-1]
print("Last chracter of your text: ",last_character)
upper_text = text.upper()
print("Upper case of your text: ",upper_text)
lower_text = text.lower()
print("Lower case of your text: ",lower_text)
"""
# ============================================================
# TAPŞIRIQ 3 — Sözün tərsinə çevrilməsi
# ============================================================

# İstifadəçidən bir söz alın və tərsinə çevirib çap edin.
#
# Nümunə:
# Python -> nohtyP
#
# İPUCU:
# slicing və mənfi step istifadə edin.

# Kodunuzu burada yazın:
"""
word = input("Enter a word: ")
print(word[::-1])
"""

# ============================================================
# TAPŞIRIQ 4 — Character sayı
# ============================================================

# İstifadəçidən bir söz və ayrıca bir character alın.
# Həmin character-in söz daxilində neçə dəfə olduğunu hesablayın.
# Böyük və kiçik hərf fərqi nəzərə alınmasın.
#
# İPUCU:
# lower(), for loop, if
# count = 0

# Kodunuzu burada yazın:
"""

word = input("Please enter a word: ")
character = input("Please enter a character: ")
word = word.lower()
character = character.lower()
count = 0
for i in range (0,len(word)):
    if(word[i] == character):
       count += 1
if (count > 0):
    print(f"the letter was found {count} times in the word")
else:
    print("Character not finded")
"""
# ============================================================
# TAPŞIRIQ 5 — Fayl növünü müəyyən edin
# ============================================================

# İstifadəçidən file name alın.
#
# .py   -> Python file
# .txt  -> Text file
# .jpg  -> Image file
# .png  -> Image file
# digər -> Unknown file type
#
# İPUCU:
# endswith(), if / elif / else, or

# Kodunuzu burada yazın:
"""
file_name = input("Please enter a file name: ")
if(file_name.endswith(".py")):
    print("Python file")
elif(file_name.endswith(".txt")):
    print("Text file")
elif(file_name.endswith(".jpg")):
    print("Image file")
elif(file_name.endswith(".png")):
    print("Image file")
else:
    print("Unknown file type")
"""
# ============================================================
# TAPŞIRIQ 6 — Command sistemi
# ============================================================

# İstifadəçidən command alın.
#
# start   -> Starting...
# stop    -> Stopping...
# restart -> Restarting...
# status  -> System is running
# digər   -> Unknown command
#
# Böyük və kiçik hərf fərqi nəzərə alınmasın.
#
# İPUCU:
# input(...).strip().lower()
# match / case istifadə edin.

# Kodunuzu burada yazın:
"""
command = input("Input a command: ").strip().lower()
match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "restart":
        print("Restarting...")
    case "status":
        print("System is running")
    case _:
        print("Unknown command")

"""
# ============================================================
# TAPŞIRIQ 7 — Password yoxlanışı
# ============================================================

# İstifadəçidən password alın.
#
# Qaydalar:
# - minimum 8 character
# - space içərməməlidir
# - daxilində ən azı bir rəqəm olmalıdır
#
# Uyğundursa:
# Strong password
#
# Əks halda:
# Weak password
#
# QEYD:
# Hazır digit-checking method keçməmisiniz.
# Rəqəmləri String kimi yoxlaya bilərsiniz:
# "0", "1", ..., "9"
#
# İPUCU:
# has_digit = False
# for char in password:
#     ...
# Rəqəm tapsanız has_digit = True edin.

# Kodunuzu burada yazın:
"""
password = input("Please enter your password: ")
while(True):
    if(len(password) >= 8 and password not in " " ):
        count = 0
        for j in range(0,10):
             if(str(j) in password):
              count += 1
        if(count>=1):
            print("Strong password")
            break
        else:
            print("Weak password")
            password = input("Please enter your password: ")
    else:
        print("Weak password")
        password = input("Please enter your password: ")
"""
# ============================================================
# TAPŞIRIQ 8 — Palindrome yoxlanışı
# ============================================================

# İstifadəçidən bir söz alın.
#
# Tərsinə oxunduqda da eynidirsə:
# Palindrome
#
# Əks halda:
# Not palindrome
#
# Böyük və kiçik hərf fərqi nəzərə alınmasın.
#
# İPUCU:
# lower(), slicing
#
# Kodunuzu burada yazın:
"""
word = input("Please enter a word: ")
word = word.lower()
rev_word = word[::-1]
if(word == rev_word):
    print("Palindrome")
else:
    print("Not polindrome")
"""
# ============================================================
# YEKUN TAPŞIRIQ — Sadə giriş sistemi
# ============================================================

# Bu məlumatlardan istifadə edin:
#
# correct_username = "admin"
# correct_password = "python123"
#
# İstifadəçiyə maksimum 3 cəhd verin.
#
# Hər cəhddə username və password daxil etsin.
#
# Username üçün:
# - əvvəl və sondakı boşluqları silin
# - böyük və kiçik hərf fərqi nəzərə alınmasın
#
# Əgər məlumatlar doğrudursa:
# Login successful
# çap edin və loop dayansın.
#
# Səhvdirsə:
# Invalid username or password
# çap edin.
#
# 3 cəhd bitdikdən sonra login alınmayıbsa:
# Too many failed attempts
# çap edin.
#
# İPUCU:
# for + range()
# if
# break
# loop else
# strip()
# lower()
# 
# Kodunuzu burada yazın:
"""
correct_username = "admin"
correct_password = "python123"
username = input("Please enter your username: ").strip().lower()
password = input("Please enter your password: ")
for i in range(0,2): 
    if(username == correct_username and password == correct_password):
        print("Login successful")
        break
    else:
        print("Invalid username or password")
        username = input("Please enter your username: ").strip().lower()
        password = input("Please enter your password: ")
else:
    print("Too many failed attempts")
"""