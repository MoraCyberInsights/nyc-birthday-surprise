import qrcode

# Replace with your deployed Streamlit app URL
app_url = "https://nyc-birthday-surprise.streamlit.app/"

qr = qrcode.make(app_url)
qr.save("birthday_qr_code.png")
print("QR code saved!")
