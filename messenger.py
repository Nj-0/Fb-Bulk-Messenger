import fbchat

client = fbchat.Client("firefisher", "RustyCrimson")

friends = client.getUsers("Revanth")  # return a list of names
friend = friends[0]
sent = client.send(friend.uid, "yo")
if sent:
    print("Message sent successfully!")