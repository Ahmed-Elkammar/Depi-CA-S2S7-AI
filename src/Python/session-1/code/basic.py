message = "###!!@mocleW EPGTQ!!!6789"
message = message[6:18]
print(message)
message = message.split() 
print(message)
message1 = message[0]
message1 = message1[::-1]
print(message1)
message2 = message[1]
message[0] = message1
message2 = message2[1:5]
print(message2)
message[1] = message2
message = " ".join(message)
print(message)
