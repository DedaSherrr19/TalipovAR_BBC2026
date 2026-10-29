
def lvl1():
    print('Уровень 1 — изменение регистра')
    print('1 — upper(): заглавные буквы')
    print('2 — lower(): строчные буквы')
    print('3 — capitalize(): первая буква заглавная')
    s=input('Введите строку: ')
    m=input('Выберите метод (1–3): ')
    if m=='1':
        print(s.upper())
    elif m=='2':
        print(s.lower())
    elif m=='3':
        print(s.capitalize())


def lvl2():
    print('Уровень 2 — поиск, подсчет, замена')
    print('1 — find(): найти позицию')
    print('2 — count(): посчитать вхождения')
    print('3 — replace(): заменить фрагмент')
    s=input('Введите строку: ')
    m=input('Выберите метод (1–3): ')
    if m=="1":
        fragment=input('Что найти? ')
        print('Певрое вхождение:',s.find(fragment))
    elif m=='2':
        fragment=input('Что посчитать? ')
        print('Количество:',s.count(fragment))
    elif m=='3':
        old=input('Что заменить? ')
        new=input('На что заменить? ')
        print(s.replace(old,new))


def lvl3():
    print('Уровень 3 — разделение, соединение')
    print('1 — split(): разделить строку')
    print('2 — join(): соединить элементы')
    print('3 — split() + join(): разделить и соединить')
    m=input('Выберите способ (1–3): ')
    if m=='1':
        s=input('Введите строку: ')
        razdel=input('По чему разделить? ')
        print(s.split(razdel))
    elif m=='2':
        s=input('Введите элементы через запятую: ')
        razdel=input('Чем соединить элементы? ')
        print(razdel.join(s.split(',')))
    elif m=='3':
        s=input('Введите строку: ')
        r1=input('По чему разделить ')
        r2=input('Чем соединить части ')
        print(r2.join(s.split(r1)))


def lvl4():
    print('Уровень 4 — тольк буквы и цифры')
    s=input('Введите строку: ')
    cl=''
    for w in s:
        if w.isalpha() or w.isdigit():
            cl+=w
    print(cl)
def lvl5():
    s='pyThOn;iS;aWeSOme'
    print(' '.join(s.upper().split(';')))

while True:
    print('Уровень (1-5). Для выхода 0')
    lvl=input()
    if lvl=='1':
        lvl1()
    elif lvl=='2':
        lvl2()
    elif lvl=='3':
        lvl3()
    elif lvl=='4':
        lvl4()
    elif lvl=='5':
        lvl5()
    elif lvl=='0':
        print('Завершено')
        break
    else:
        print('Введите число от 0 до 5')