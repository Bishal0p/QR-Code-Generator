import qrcode

#Taking upi id as a input
upi_id = input("Enter the UPI ID = ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=currency&tn=message
#Defining the payment URL based on the UPI ID and payment app
#You can modify these URL based ont the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=RecipientName&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=RecipientName&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=RecipientName&mc=1234'

#create QR code for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#we can save this QR code to image file
# phonepe_qr.save('phonepe_qr.png')
# paytm_qr.save('paytm_qr.png')
# google_pay_qr.save('google_pay_qr.png')

#To display QR code we used pillow library
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
