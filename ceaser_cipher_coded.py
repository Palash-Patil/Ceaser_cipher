'''This is an illustration of Julias Ceaser's epic cipher he used to code his military messages 
though this is not used anywhere in cryptography today, yet it's building block for ciphers like  Vigenère cipher, and still has modern application in the ROT13 system'''
ch=int(input('enter your choice:  1:cipher \n\t\t\t\t\t2:decipher \n\t\t\t\t\t3:exit\n'))

while(0<ch<3):
    if(ch==1):
#declaring alphabetical serries
        alpha_lower='abcdefghijklmnopqrstuvwxyz'
        alpha_caps='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nums='1234567890'
        othr=' ,!@#$%6&*(){}[]/\|=+-_<>?;:"\''
        s= input('Enter the string to be ciphered here: ')    
        t=''
        l=len(s)    
#k stands for key by which a given character will be changed in cipher
#Ceaser used this value as 3
        k=3
#juggling the given characters with a key value       
        for i in range(l):
            if(s[i] in othr):
                t=t+s[i]
            elif(s[i] in alpha_lower):
                t=t+alpha_lower[(((alpha_lower.index(s[i]))+k)%26)]
            elif(s[i] in alpha_caps):
                t=t+alpha_caps[(((alpha_caps.index(s[i]))+k)%26)]
            elif(s[i] in nums):
                t=t+nums[(((nums.index(s[i]))+k)%10)]
    
        print('Ceaser_Cipher for given string is: ',t)
        ch=int(input('enter your choice:  1:cipher \n\t\t\t\t\t2:decipher\n'))
    
    if(ch==2):
#declaring alphabetical serries
        alpha_lower='abcdefghijklmnopqrstuvwxyz'
        alpha_caps='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nums='1234567890'
        othr=' ,!@#$%6&*(){}[]/\|=+-_<>?;:"\''
        s= input('Enter the string to be deciphered here: ')    
        t=''
        l=len(s)
#k stands for key by which a given character will be changed in cipher
#Ceaser used this value as 3
        k= 3
#juggling the given characters with a key value 
        for i in range(l):
            if(s[i] in othr):
                t=t+s[i]
            elif(s[i] in alpha_lower):
                t=t+alpha_lower[(((alpha_lower.index(s[i]))-k)%26)]
            elif(s[i] in alpha_caps):
                t=t+alpha_caps[(((alpha_caps.index(s[i]))-k)%26)]
            elif(s[i] in nums):
                t=t+nums[(((nums.index(s[i]))-k)%10)]
    
        print('The string is: ',t)
        ch=int(input('enter your choice:  1:cipher \n\t\t\t\t\t2:decipher\n'))
        