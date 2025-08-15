a=input('Enter the text:')
b=''
c=''
for i in a:
    if i.lower() in('a','e','i','o','u',' '):
        pass
    else:
        b+=i
for j in a:
    if j.lower() not in ('a','e','i','o','u',' '):
        pass
    else:
        c+=j
print('The no.of vowels in the given text:',len(c))
print('The no.of consonents in the given text:',len(b))
