import streamlit as st
import smtplib
from email.message import EmailMessage

st.title("Email Sender App")

email_sender = st.text_input("Sender Email")
receive_email = st.text_input("Receiver Email")
password = st.text_input("App Password", type="password")

subject = st.text_input("Subject")
message_text = st.text_area("Message")

if st.button("Send Email"):

    if not email_sender or not receive_email or not password:
        st.error("Please enter sender email, receiver email and app password.")

    else:
        message = EmailMessage()

        message["Subject"] = subject
        message["From"] = email_sender
        message["To"] = receive_email

        message.set_content(message_text)

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(email_sender, password)
                smtp.send_message(message)

            st.success("Email sent successfully! ✅")

        except Exception as e:
            st.error(f"Email could not be sent: {e}")