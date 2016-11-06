import fbchat
import re

def getFriendListRaw():

	fileData = open('raw.txt', 'r')
	friendFile = open('friend.txt', 'w')
	friendList=[]
	for line in fileData:

	  matchFriendLiteral = re.search('[^\n]*[fF]riend', line)
	  matchDesc=re.search('        ', line)

	  if matchFriendLiteral or matchDesc :
	  	continue
	  elif line!='\n':
	  	friendList.append(line.strip())
		friendFile.write("%s\n" % line.strip())

	print "Generated friends.txt"

	return friendList

def getFriendList():

	fileData = open('friend.txt', 'r')
	friendList=[]
	for line in fileData:
	  	friendList.append(line.strip())

	return friendList


try:
    f = open('friend.txt')
    friendList = getFriendList()
except IOError:
    try:
    	f = open('raw.txt')
    	friendList = getFriendListRaw()
    except IOError:
    	print 'Oh dear. Can not find the raw '
    	exit()


client = fbchat.Client("Your_Username", "Your_Password")

for username in friendList:
	friends = client.getUsers(username)  # return a list of names
	if friends:
		friend=friends[0].uid
		sent = client.send(friend, "Hi :)")
		if sent:
			print "message sent to " + username
