import qrcode
import json

qr = qrcode.QRCode(version=1, box_size=10, border=5)

with open("data.json", "r", encoding="UTF-8") as fhand:
    data = json.load(fhand)

color = data["qrCodeColor"]
bg_color = data["qrCodeBackgroundColor"]

all_staff = data["staff"]
for staff in all_staff:

    vcard = f"""BEGIN:VCARD
VERSION:4.0
FN:{staff['name']}
ORG:{data["company"]}
TITLE:{staff['title']}
TEL;TYPE=WORK,VOICE:{staff['phone']}
EMAIL;TYPE=PREF,INTERNET:{staff['mail']}
URL:{data["website"]}
END:VCARD"""

    vcard = vcard.encode('utf-8').decode('utf-8')
    qr.add_data(vcard)

    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color=bg_color)
    names = staff['name'].replace(' ', '_')
    img.save(f"qr-codes/vCard-{names}.png")
    qr.clear()
    print(f"Created: QR-code --> {names}.png")
