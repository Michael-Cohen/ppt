def say_hello_with_message(msg):
    print(f"hello, the message is: {msg}")

print("voilà")
print("je suis à la maison")

def wow(msg):
    say_hello_with_message(f"wow: {msg}")

if __name__ == '__main__':
    say_hello_with_message(1)