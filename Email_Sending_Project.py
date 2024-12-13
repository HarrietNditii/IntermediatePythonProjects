import smtplib
from email.message import EmailMessage
from tkinter import Tk, Label, Entry, Text, Button, StringVar, filedialog, OptionMenu, messagebox
import os

#Function to send email
def send_email():
    try:
        smtp_server = smtp_var.get()
        smtp_port = 587 if smtp_server == 'Gmail' else 465
        email_address = sender_email.get()
        email_password = sender.password.get()
        recepient = recepient_email.get()
        subject = subject_entry.get()
        body = body_text.get("1.0", "end").strip()
        attachment_path = attachment_var.get()

        #validate inputs
        if not email_address or not email_password or not recepient or not subject or not body:
            messagebox.showerror("Error", "All fields except attachment are mandatory!")
            return

        #create email
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = email_address
        msg['To'] = recepient
        msg.set_content(body)

        #Add attachment if provided
        if attachment_path:
            try:
                with open(attachment_path, 'rb') as file:
                    file_data = file.read()
                    file_name = os.path.basename(attachment_path)
                    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to attach file: {e}")
                return

        #connect to SMTP server and send email
        smtp_host = 'smtp.gmail.com' if smtp_server == 'Gmail' else 'smtp.mail.yahoo.com'

        with smtplib.SMTP(smtp_host, smtp_port) as smtp:
            smtp.starttls() #secure the conection
            smtp.login(email_address, email_password)
            smtp.send_message(msg)

        messagebox.showinfo("Success", "Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Error", "Authentication failed. Check your email and password.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occured: {e}")
    

#function to select attachment file
def select_attachment():
    file_path = filedialog.askopenfilename()
    attachment_var.set(file_path)

#initialize GUI application
app = Tk()
app.title("Email Sender")
app.geometry("500x500")

#Gui elements
Label(app, text="SMTP Server:").grid(row=0, column=0, pady=5, padx=10, sticky="W")
smtp_var = StringVar(app)
smtp_var.set("Gmail") #Default value
smtp_menu = OptionMenu(app, smtp_var, "Gmail", "Yahoo")
smtp_menu.grid(row=0, column=1, pady=5, padx=10, sticky="W")

Label(app, text="Sender Email:").grid(row=1, column=0, pady=5, padx=10, sticky="W")
sender_email = Entry(app, width=40)
sender_email.grid(row=1, column=1, pady=5, padx=10)

Label(app, text="Password:").grid(row=3, column=0, pady=5, padx=10, sticky="W")
sender_password = Entry(app, show="*", width=40)
sender_password.grid(row=2, column=1, pady=5, padx=10)

Label(app, text="Recepient Email:").grid(row=3, column=0, pady=5, padx=10, sticky="W")
recepient_email = Entry(app, width=40)
recepient_email.grid(row=3, column=1, pady=5, padx=10)

Label(app, text="Subject:").grid(row=4, column=0, pady=5, padx=10, sticky="w")
subject_entry = Entry(app, width=40)
subject_entry.grid(row=4, column=1, pady=5, padx=10)

Label(app, text="Body:").grid(row=5, column=0, pady=5, padx=10, sticky="nw")
body_text = Text(app, height=10, width=40)
body_text.grid(row=5, column=1, pady=5, padx=10)

Label(app, text="Attachment:").grid(row=6, column=0, pady=5, padx=10, sticky="w")
attachment_var = StringVar()
attachment_entry = Entry(app, textvariable=attachment_var, width=30, state="readonly")
attachment_entry.grid(row=6, column=1, pady=5, padx=10, sticky="w")
attachment_button = Button(app, text="Browse", command=select_attachment)
attachment_button.grid(row=6, column=1, pady=5, padx=10, sticky="e")

send_button = Button(app, text="Send Email", command=send_email, bg="blue", fg="white")
send_button.grid(row=7, column=1, pady=20, padx=10, sticky="e")

# Run the application
app.mainloop()
