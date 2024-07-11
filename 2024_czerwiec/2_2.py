#F(64)=2+F(32)=2+2+F(16)=2+2+2+F(8)=8+F(4)=10+F(2)=12+F(0)=14
#F(256)=2+F(128)=4+F(64)=6+F(32)=8+F(16)=10+F(8)=12+F(4)=14+F(2)=16+F(0)=18
#F(35)=2+f(17)=4+f(16)
def F(x):
    if x==0:
        return 0
    else:
        return 2+F(x//2)
print(F(511))
#najmniejszy 256
#największy 511

#ok nie wiem co się stało, jak widać po obliczeniach wpadłem na pomysł kalkulatora
#robiłem wszystko tak jak w rozwiązaniu ale zapomniałem return więc nie wychodziło mi
#potem spróbowałem while x!=0 i chodziło mi w nieskończoność
#jedynym błędem był brak return
#czy ja mam to zaliczyć???
