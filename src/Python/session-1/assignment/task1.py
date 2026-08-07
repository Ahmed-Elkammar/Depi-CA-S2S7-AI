mail = "Amit_ml@gmail.com"

if mail.count("@") ==1 and mail[mail.index("@") + 1:].find(".") != -1:
    print("Valid email address")
    at_index = mail.index("@")
    dot_index = mail.index(".")

    user = mail[:at_index]
    print("Username:", user)
    domain = mail[at_index + 1:dot_index]
    print (domain)

    domain_end = mail[dot_index:]
    if domain_end == ".com":
        print("Commercial Domain")

    elif domain_end == ".edu":
        print("Educational Domain")

    else:
        print("Other Domain")

else:
    print("Invalid email address")


