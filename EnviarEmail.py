import smtplib
from email.message import EmailMessage

# Configuración del correo
email_origen = "ezequielcantarero@gmail.com"
email_destino = "ezequielcantarero@gmail.com"
contraseña = "kelt nolu hwky gvkn"  # Usa la clave generada en Google

# Crear el mensaje
mensaje = EmailMessage()
mensaje["Subject"] = "Prueba de correo automático"
mensaje["From"] = email_origen
mensaje["To"] = email_destino
mensaje.set_content("Este es un correo enviado con Python.")

# Enviar el correo
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(email_origen, contraseña)
    smtp.send_message(mensaje)

print("Correo enviado con éxito!")
