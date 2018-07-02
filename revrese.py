text = raw_input("Enter a string of your choice:")

def reverse(stri):
    word = " "
    x= len(stri)-1
    for i in range(0, len(stri)):
        word= word+stri[x]
        x-=1
    print word

reverse(text)
    
