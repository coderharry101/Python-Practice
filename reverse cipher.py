text = 'Hello This is an urgent message!'

reverse = ''

i = len(text)-1
while i >= 0:
    reverse = reverse+text[i]
    i = i-1

print('Reversed string is', reverse)
