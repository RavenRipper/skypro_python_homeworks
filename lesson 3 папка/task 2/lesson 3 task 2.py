from smartphone import Smartphone

catalog = []
phone1 = Smartphone ("Samsung", "Galaxy 521", "791234567891")
phone2 = Smartphone ("Apple", "iPhone 12", "+79098765432")
phone3 = Smartphone ("Xiaomi", "ML 11", "+79876543218")
phone4 = Smartphone ("Google", "Pixel 5", "+79765432189")
phone5 = Smartphone ("OnePlus", "9 Pro", "+796543218987")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")