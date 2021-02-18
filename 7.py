import smtplib as sm 
email = '#Your E-mail'    
 
Server = sm.SMTP('smtp.gmail.com', 587)
Server.starttls()
Server.login('#Your E-mail', '#Your password')

print('='*15)
print('Connected!')
print('='*15)

e_mail = input(' Send e_mail > ')
mess = input(' Message >  ')
    
Server.sendmail(email, e_mail, mess)
print(f'Email has been send to {e_mail}')