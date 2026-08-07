message = ("&&&**$gnirtS PLIO!!@1234 ")
message = message[6:17]
print(message)

message = message.split()
message1 = message[0]
message2 = message[1] 

message1 = message1[::-1]
print(message1)
message2 = message2.replace("I","E").replace("O","U")
print(message2)
message = message1 + " " + message2
print(message)



