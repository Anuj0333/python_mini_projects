
try:
    file=open("a_file.txt")
    a_dictionary={"anuj":"value"}
    print(a_dictionary["anuj"])
except FileNotFoundError:
    file=open("a_file.txt","w")
    file.write("something")
except KeyError as error_message:
    print(f"the key {error_message} does not exist")
else:
    content=file.read()
    print(content )
finally:  
    file.close()
    print("file was closed")
    raise TypeError("this is the error that i made up")