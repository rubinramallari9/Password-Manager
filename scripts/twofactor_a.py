import smtplib
import random

company_email = "" # => Your email
company_password = "" # => Your app password

letters = "q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m".split(",")
numbers = [1,2,3,4,5,6,7,8,9,0]

def create_verification_code():
    random_letters = [random.choice(letters) for i in range(3)]
    random_numbers = [random.choice(numbers) for j in range(3)]
    random_code = random_numbers+random_letters

    return random.shuffle(random_code)

def send_verifcationCode(user_email: str):
    code = create_verification_code()
    content = None
    with smtplib.SMTP(host="stmp.gmail.com", port=578) as connection:
        connection.starttls()
        connection.login(company_email, company_password)
        connection.sendmail(from_addr=company_email, to_addrs=user_email, msg=code)