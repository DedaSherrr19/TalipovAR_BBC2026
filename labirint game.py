from random import randint
n,m=map(int,input('размер лабиринта: ').split())
x,y=map(int,input('спавн (от 0): ').split())
hp=int(input('хп: '))
max_hp=hp
inv=[]
coins=0
win=False
lab=[[' . ' for i in range(m)] for i in range(n)]
lab2=[[' . ' for i in range(m)] for i in range(n)]
lab2[x][y]='spawn'
#выход
while True:
    tr_x=randint(0,n-1)
    tr_y=randint(0,m-1)
    if lab2[tr_x][tr_y]==' . ':
        lab2[tr_x][tr_y]='exit'
        lab[tr_x][tr_y]=' E '
        break
#монеты
for i in range(5):
    while True:
        coin_x=randint(0,n-1)
        coin_y=randint(0,m-1)
        if lab2[coin_x][coin_y]==' . ':
            lab2[coin_x][coin_y]='coin'
            break
treasure_n=n*m//10
#сундуки
for i in range(treasure_n):
    while True:
        tr_x=randint(0,n-1)
        tr_y=randint(0,m-1)
        if lab2[tr_x][tr_y]==' . ':
            lab2[tr_x][tr_y]=['med','armor']
            break
#враги
for i in range(n*m//5):
    while True:
        tr_x=randint(0,n-1)
        tr_y=randint(0,m-1)
        if lab2[tr_x][tr_y]==' . ':
            lab2[tr_x][tr_y]='enemy'
            break


def show():
    for i in range(n):
        for j in range(m):
            if i==x and j==y:
                #print(' M ',end='')
                print(' \033[35mM\033[0m ',end='')#\e[0;35m
            else:
                print(lab[i][j],end='')
        print()

    print('хп',hp,'/',max_hp)
    print('монеты',coins,'/ 5')


def move(i,j):
    global x,y,hp,coins,win

    if 0<=x+i<n and 0<=y+j<m:
        if lab[x][y]==' . ':
            lab[x][y]=' o '
        x+=i
        y+=j
        if isinstance(lab2[x][y],list):
            inv.extend(lab2[x][y])
            print('в сундуке аптечка и броня')
            lab[x][y]=' \033[33mc\033[0m '
            lab2[x][y]=' . '

        elif lab2[x][y]=='coin':
            coins+=1
            inv.append('coin')
            print('монета найдена')
            lab[x][y]=' \033[32m$\033[0m '
            lab2[x][y]=' . '

        elif lab2[x][y]=='enemy':
            hp=max(0,hp-5)
            print('враг')
            lab[x][y]=' \033[31mx\033[0m '
            lab2[x][y]=' . '

        elif lab2[x][y]=='exit':
            if coins==5:
                win=True
            else:
                print('нужны все пять монет')

    else:
        print('стена, - 1 хп')
        hp-=1
show()

while hp>0 and not win:
    step=input('w/a/s/d/ — ход, i инвентарь, h аптечка, b броня: ')

    if step=='w':
        move(-1,0)
    elif step=='s':
        move(1,0)
    elif step=='a':
        move(0,-1)
    elif step=='d':
        move(0,1)

    elif step=='i':
        print('инвентарь:',inv)
    elif step=='h':
        if 'med' in inv:
            if hp<max_hp:
                hp=min(hp+5,max_hp)
                inv.remove('med')
                print('аптечка использована')
            else:
                print('хп полное')
        else:
            print('нет аптечки')

    elif step=='b':
        if 'armor' in inv:
            max_hp+=5
            hp+=5
            inv.remove('armor')
            print('броня, +5 макс хп')
        else:
            print('нет брони')

    show()

if win:
    print('ты прошел игру, молодец')
else:
    print('поражение')
    print('чтобы продолжить, переведите 10$ на TPH3ggvAjPdo7nBsMYkpmSepb4JGBza67Q')