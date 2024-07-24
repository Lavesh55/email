import smtplib
server=smtplib.SMTP(host="smtp.gmail.com",port=587) #smtp ka kam krata h port=0 to 656508
server.starttls()# start the server
receiver_email=input("Enter the email")
sender_email="laveshgurjar71@gmail.com"
sender_password="pobk umvw xzow qfgc"
server.login(sender_email,sender_password)
subject=input("what is your problem")
Body=input("body")
message=f"subject: {subject}\n\n{Body}"
server.sendmail(sender_email,receiver_email,message)
print("send ho gyi h")
server.quit()