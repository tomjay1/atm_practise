#ATM PRACTISE

print ('input login details')

name = input ('what is your name? \n')
allowedusers = ['tomjay','seyi','mike','efe']
allowedpassword ='tominio'
if(name in allowedusers):
    password = input ('your password \n')

    if(password in allowedpassword):
        print ('welcome %s' 'name')
    else:
        print('password incorrect, please try again')
    

else:
    print ('name not found, please try again')
    
print ('input login details')

name = input ('what is your name? \n')
allowedusers = ['tomjay','seyi','mike','efe']
allowedpassword =['tominio','calida','wifi', 'comein']

if(name in allowedusers):
    password = input ('your password \n')
    userID = allowedusers.index(name)

    if(password in allowedpassword[userID]):
        print ('welcome %s' % name)
       
        print ('1.withdrawal')
        print ('2. deposite')
        print ('3.any complain')
        selectedoption = int(input ('please select an option \n'))

        if(selectedoption == 1):
            print('input withdral amount \n')            
        elif(selectedoption == 2):
            print('input deposite amount \n ')
        elif(selectedoption == 3):
            print('input complain? \n ')
        else:
            print ('invalid option selected, please try again')
    else:
        print('password incorrect, please try again')
else:
    print ('name not found, please try again')

print  ('1. #5000')
print  ('2. #10000')
print  ('3. #15000')
selectedOption = int(input ('plases select an option \n'))

if(selectedOption ==1):
    print ('loading... take your cash, thank you')
elif(selectedOption ==2):
        print ('loading... take cash, thanks')
elif (selectedOption ==3):
        print ('accepted payment')