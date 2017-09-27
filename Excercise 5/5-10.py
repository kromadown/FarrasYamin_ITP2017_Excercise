current_users = ['ana','admin','bob','charlie','george']
new_users = ['Ana','Lee','heen','BoB','mark']

for i in new_users:
    if i.casefold() in current_users:
        print ('Enter a new username')
    else:
        print ('Username is available')
