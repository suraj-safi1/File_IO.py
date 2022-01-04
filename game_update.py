def game():
    return 889
score=game()
with open ('hisscore.txt') as f:
    hisscore=f.read()
if hisscore =='':
    with open ('hisscore.txt','w') as f:
        f.write(str(score))
elif int(hisscore )< score:
    with open ('hisscore.txt','w') as f:
        f.write(str(score))
