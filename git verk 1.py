#dæmi1
'''
tala1=int(input("sláðu inn tölu"))
tala2=int(input("sláðu inn aðra tölu"))
marg=tala1*tala2
plus=tala1+tala2
print("tölurnar lagðar saman = "+str(plus)+" tölurnar margfaldaðar saman = "+str(marg))



#dæmi 2

fornafn=input("slaðu inn fornafn ")
eftirnafn =input("sláðu inn eftirnafn ")
print("halló "+fornafn,eftirnafn)
'''
#dæmi3
hair=0
lair=0
strax=0
eftir = 0
texti=input("sláðu inn texta")
for x in range(len(texti)):
    if texti[x].isupper():
        hair=hair+1
    if texti[x].islower():
        lair=lair+1
        if x != 0 and texti[x-1].isupper():
            eftir += 1

print("í þessum texta eru "+str(hair)+" háir stafir og "+str(lair)+"lágstafir og "+str(eftir)+" lágstafir koma strax á eftir hástaf.")
