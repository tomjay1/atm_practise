#ATM PRACTISE

#print ('input login details')

#name = input ('what is your name? \n')
#allowedusers = ['tomjay','seyi','mike','efe']
#allowedpassword ='tominio'
#if(name in allowedusers):
    #password = input ('your password \n')

    #if(password in allowedpassword):
        #print ('welcome %s' 'name')
    #else:
        #print('password incorrect, please try again')
    

#else:
    #print ('name not found, please try again')
    
print ('input login details')

name = input ('what is your name? \n')
allowedusers = ['tomjay','bimpe','mike','efe']
allowedpassword =['tmoney','bmoney','wifi', 'comein']

if(name in allowedusers):
    password = input ('your password \n')
    userID = allowedusers.index(name)

    if(password in allowedpassword[userID]):
        print ('welcome %s' % name)
        import datetime
        now = datetime.datetime.now()   
        #print ('current date and time :')
        print (now.strftime('%Y/%m/%d %H:%M:%S'))
        print ('current balance #50000 ')
        print ('proceed and select an option')
        print ('1. withdrawal')
        print ('2. deposit')
        print ('3. any complain')
        selectedoption = int(input ('input selected an option \n'))
                #withdrawal
        if(selectedoption ==1):
            print ('select amount to withdraw')
            print  ('1. #10000')
            print  ('2. #20000')
            print  ('3. #30000')
            selectedOption = int(input ('input selected option \n'))
                
            if(selectedOption ==1):
             print ('dispensing... take your cash,\ current balance #40000, \ thank you')
            elif(selectedOption ==2):
             print ('dispensing... take your cash,\ current balance #30000, \ thank you')
            elif (selectedOption ==3):
             print ('dispensing... take your cash,\ current balance #20000, \ thank you')
                #deposit
        elif(selectedoption ==2):
            print ('select amount to deposit')
            print  ('1. #10000')
            print  ('2. #15000')
            print  ('3. #25000')
            selectedOption = int(input ('input selected option \n'))
                
            if(selectedOption ==1):
             print ('account credited \ current balance #60000,\ thank you')
            elif(selectedOption ==2):
             print ('account credited \ current balance #65000,\ thank you ')
            elif (selectedOption ==3):
             print ('account credited \ current balance #75000,\ thank you')
                #complain
        elif (selectedoption ==3):
            print ('what issue will you like to report')
            print  ('1. lost atm card/lost token')
            print  ('2. pos purchase error ')
            print  ('3. unathorized transaction')
            selectedOption = int(input ('input selected option \n'))
                
            if(selectedOption ==1):
             print ('kindly visit the nearest branch to request for a new device, thanks')
            elif(selectedOption ==2):
             print ('kindly visit our website, thank you')
            elif (selectedOption ==3):
             print ('kindly get a police report and visit the nearest branch, thank you')
            
        else:
            print ('invalid option selected, please try again')
    else:
            print('password incorrect, please try again')
else:
    print ('name not found, please try again')

#print  ('1. #5000')
#print  ('2. #10000')
#print  ('3. #15000')
#selectedOption = int(input ('input selected option \n'))

#if(selectedOption ==1):
  #  print ('loading... take your cash,\ thank you')
#elif(selectedOption ==2):
   #     print ('loading...\ current balance #20000,\ thanks')
#elif (selectedOption ==3):
 #       print ('thank you for contacting us')
