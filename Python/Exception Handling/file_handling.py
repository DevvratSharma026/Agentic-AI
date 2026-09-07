# to open a file use open(): with filename and path

# try:
#     file = open("order.txt", "w")
#     file.write("Hello World!")
# finally:
#     file.close()


# NEW WAY 
with open("order.txt", "w") as file:
    file.write("Hellooo World!!")