import tkinter as tk
from tkinter import *
import random
import smtplib

# Generate a 6-digit random OTP
def generate_otp():
    otp = random.randint(100000, 999999)
    return str(otp)

# Send OTP via email
def send_email(email, otp):
    try:
        smtp_server = "smtp.gmail.com"
        port = 587

        sender_email = "snehitgawand345@gmail.com"
        sender_password = "cnxb hllf tcjx qrra"  

        receiver_email = email
        subject = "OTP Verification"
        message = f"Your OTP is: {otp}"

        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, sender_password)

        server.sendmail(sender_email, receiver_email, f"Subject: {subject}\n\n{message}")
        server.quit()

        return True
    except Exception as e:
        print("Error sending email:", str(e))
        return False

# Verify OTP
def verify_otp(entered_otp):
    if entered_otp == otp:
        result_label.config(text="OTP Verified Successfully!")
    else:
        result_label.config(text="OTP Verification Failed. Try Again.")

# GUI Setup
window = tk.Tk()
window.title("OTP Verification App")
window.geometry('400x300')
window.configure(bg='seashell4')

otp = generate_otp()

title_label = Label(window, text='OTP Verification', font=('Helvetica', 20, 'bold'), bg='seashell4')
title_label.pack(pady=10)

email_label = Label(window, text='Enter Your Email:', font=('Helvetica', 15, 'bold'), bg='seashell4')
email_label.pack()

email_entry = tk.Entry(window, width=30)
email_entry.pack(pady=5)

send_button = tk.Button(window, text="Send OTP", command=lambda: send_email(email_entry.get(), otp))
send_button.pack(pady=5)

otp_label = Label(window, text='Enter OTP Received:', font=('Helvetica', 15, 'bold'), bg='seashell4')
otp_label.pack()

otp_entry = tk.Entry(window, width=30)
otp_entry.pack(pady=5)

verify_button = tk.Button(window, text="Verify OTP", command=lambda: verify_otp(otp_entry.get()))
verify_button.pack(pady=5)

result_label = tk.Label(window, width=30, text="", font=('Helvetica', 12), bg='white')
result_label.pack(pady=10)

window.mainloop()
