
word = str(input('input your word:   ')) 
secrecy = {a: False for a in word}
box = []
for i in word:
    box.append(i)

answer = {a: '_ ' for a in word}
gg = 0
finish = False

def ggwp():
    if gg == 1:
        print("    O    ")
    elif gg == 2:
        print("    O    ")
        print("   /|\    ")
    elif gg == 3:
        print("    O    ")
        print("   /|\    ")
        print('   / \  ')
        finish = True
        print(' game over')

while finish == False:
    test = str(input('go input:   '))
    if test in box:
        print('true')
        for i in box:
            if i == test:
                if secrecy[i] != True:          
                    secrecy[i] = True                
                    answer[i] = i
                    p = answer.values()
                    print(p)
                    if '_ ' not in p:
                        print('you victory')
                        finish = True
            
                else:
                    print('false')    
                    gg += 1
                    ggwp()
                                    
    else:
        print('false')
        gg += 1
        ggwp()
        
 