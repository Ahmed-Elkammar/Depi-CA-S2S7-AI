message = "##$$$@!yalpstcejorp EPUVT****9887"
message = message[7:25]
print(message)
message = message.split()

message1 = message[0]
message1 = message1[::-1]
print(message1)
message2 = message[1]
message2 = message2.replace("E","A").replace("U","O")
print(message2)
message =" ".join([message1,message2])
print(message)