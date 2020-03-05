import time,random

def rand(a,b):
    return random.randint(a,b)

def stat(hp,food,sleep,biom):
    print('Your stats:')
    print('Food: '+str(food))
    print('Sleep: '+str(sleep))
    print('HP: '+str(hp))
    print('Biom:'+biom)

def combat(name,maxdam,mindam,hpdam):
    while True:
        stat(hp,food,sleep,'fight')
        if hp<0:
            print('Dead...')
            exit()
            break
        if food<0:
            print('Food is low! -1 hp')
            hp-=1
        if hpdam<0:
            print('You win!')
            break
        print('You has attacked by '+name+'! Fight!!!')
        print('1.block')
        print('2.heal')
        print('3.punch')
        a=input('>')
        if a=='1':
            if rand(0,1)==1:
                b=rand(mindam,maxdam)
                hp-=b
                print('Fail... -'+b+'hp')
            else:
                print('You blocked punch!')
        if a=='2':
            if rand(0,1)==1:
                b=rand(mindam,maxdam)
                print('Fail... -'+b+'hp')
            else:
                b=rand(1,10)
                food-=rand(1,5)
                print('You healed! +'+b+'hp!')
        if a=='3':
            if rand(0,1)==1:
                b=rand(mindam,maxdam)
                print('Fail... -'+b+'hp')
            else:
                b=rand(1,10)
                food-=rand(1,5)
                hpdam-=b
                print('You punch! '+name+'-'+b+'hp!')
        
            
    

hp=50
bioms=['forest','sand','onion','mushroom','canyon','snow','tropical']
biom=bioms[0]
food=100
sleep=0
score=0

while True:
    print('')
    stat(hp,food,sleep,biom)
    print('Your score:'+str(score))
    print('1.walk')
    print('2.sleep')
    print('3.eat')
    print('4.exit')
    a=input('>')
    if a=='1':
        biom=bioms[rand(0,6)]
        sleep+=rand(1,5)
        food-=rand(1,5)
        b=rand(0,1)
        if b==0:
            name='monster'
            maxdam=5+food//100
            mindam=1
            hpdam=10
            while True:
                print('')
                stat(hp,food,sleep,'fight')
                if hp<0:
                    print('Dead...')
                    exit()
                    break
                if food<0:
                    print('Food is low! -1 hp')
                    hp-=1
                if hpdam<0:
                    print('You win!')
                    break
                print('You has attacked by '+name+'! Fight!!!')
                print('1.block')
                print('2.heal')
                print('3.punch')
                a=input('>')
                if a=='1':
                    if rand(0,1)==1:
                        b=rand(mindam,maxdam)
                        hp-=b
                        print('Fail... -'+str(b)+'hp')
                        hp-=b
                    else:
                        print('You blocked punch!')
                if a=='2':
                    if rand(0,1)==1:
                        b=rand(mindam,maxdam)
                        hp-=b
                        print('Fail... -'+str(b)+'hp')
                    else:
                        b=rand(1,10)
                        food-=rand(1,5)
                        hp+=b
                        print('You healed! +'+str(b)+'hp!')
                if a=='3':
                    if rand(0,1)==1:
                        b=rand(mindam,maxdam)
                        hp-=b
                        print('Fail... -'+str(b)+'hp')
                    else:
                        b=rand(1,10)
                        food-=rand(1,5)
                        hpdam-=b
                        print('You punch! '+name+'-'+str(b)+'hp!')
    if a=='2':
        b=rand(0,1)
        if b==0:
            name='monster'
            maxdam=5
            mindam=1
            hpdam=10
            while True:
                print('')
                stat(hp,food,sleep,'fight')
                if hp<0:
                    print('Dead...')
                    exit()
                    break
                if food<0:
                    print('Food is low! -1 hp')
                    hp-=1
                if hpdam<0:
                    print('You win!')
                    break
                print('You has attacked by '+name+'! Fight!!!')
                print('1.block')
                print('2.heal')
                print('3.punch')
                a=input('>')
                if a=='1':
                    if rand(0,1)==1:
                        b=rand(mindam,maxdam)
                        hp-=b
                        print('Fail... -'+str(b)+'hp')
                        hp-=b
                    else:
                        print('You blocked punch!')
                if a=='2':
                    if rand(0,1)==1:
                        b=rand(mindam,maxdam)
                        hp-=b
                        print('Fail... -'+str(b)+'hp')
                    else:
                        b=rand(1,10)
                        food-=rand(1,5)
                        hp+=b
                        print('You healed! +'+str(b)+'hp!')
                if a=='3':
                    if rand(0,1)==1:
                        b=rand(mindam,maxdam)
                        hp-=b
                        print('Fail... -'+str(b)+'hp')
                    else:
                        b=rand(1,10)
                        food-=rand(1,5)
                        hpdam-=b
                        print('You punch! '+name+'-'+str(b)+'hp!')
        else:
            print('You sleeps...')
            sleep-=5
    if a=='3':
        if biom!='sand' or biom!='canyon' or biom!='snow':
            food+=5
            print('You eats...')
        else:
            print('No food here...')
    if a=='4':
        break
    score+=1
    if rand(0,1)==1:
        hp+=2
        
