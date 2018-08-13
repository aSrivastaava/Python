def check(string):
    vowels = "a,e,i,o,u,A,E,I,O,U"
    special = "`,~,!,@,#,$,%,^,&,*,(,),_,+,=,-"
    consonents = "b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z"
    numbers = "0,1,2,3,4,5,6,7,8,9"

    num_vowels=0
    num_special=0
    num_Consonents=0
    num_numbers=0
    for j in string:
        if(j in vowels):
            num_vowels = num_vowels + 1
    for k in string:
        if(k in special):
            num_special = num_special + 1
    for o in string:
        if(o in consonents):
            num_Consonents = num_Consonents + 1
    for p in string:
        if(p in numbers):
            num_numbers = num_numbers + 1
