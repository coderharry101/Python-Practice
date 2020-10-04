#################################
# Program to reverse the string #
#################################

text = 'Hello This is an urgent message!'

# Easy approach
reverse = text[::-1]
'''
i = len(text)-1
while i >= 0:
    reverse = reverse+text[i]
    i = i-1
'''
print('Reversed string:', reverse)
