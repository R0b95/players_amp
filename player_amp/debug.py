# UsercountAmp
### written in Phyton 3.8.1 by Strolch

import os.path
import re

from appdirs import user_config_dir

from player_amp import api_functions


# reads settings.txt and save the data

def debug():
    filename = "settings.txt"
    path = user_config_dir(appauthor="Strolch", appname="playeramp", roaming=False)
    filepath = os.path.join(path, filename)

    file = open(filepath, mode='r')
    settings = re.findall(r'"(.*?)"', file.read())
    file.close()

    server = settings[0]
    port = settings[1]
    username = settings[2]
    password = settings[3]
    header = {'Accept': 'application/json'}

    sessionid = api_functions.Login.session_id(server, port, username, password, header)
    instanceids = api_functions.GetInstances.instance_ids(server, port, header, sessionid)
    sessionids = api_functions.Login.session_ids(server, port, username, password, header, instanceids)
    usercount = api_functions.GetUpdates.usercount(server, port, header, sessionids, instanceids)

    print("session id der Mainpage ist: " + sessionid)

    i = 1
    while i < len(instanceids):
        print("instance id [" + str(i) + "] ist: " + instanceids[i])
        i += 1

    i = 1
    while i < len(sessionids):
        print("session id [" + str(i) + "] ist: " + sessionids[i])
        i += 1

    logouts = api_functions.Logout.instances(server, port, header, instanceids, sessionids)
    i = 0
    while i < len(logouts):
        if (logouts[i]).content == b'null':
            print("Logout bei Instance " + str(i) + " erfolgreich!")
        else:
            print("Error beim Logut der Mainpage!")
        i += 1

    logout = api_functions.Logout.main(server, port, header, sessionid)
    if logout.content == b'null':
        print("Logout auf der Mainpage erfolgreich!")
    else:
        print("Error beim Logut der Mainpage!")

    if usercount == 0:
        print("\nEs ist kein User auf den Gamingservern unterwegs!")
        print(usercount)
    elif usercount == 1:
        print("\nEs ist 1 User auf einem der Gamingserver unterwegs!")
        print(usercount)
    else:
        print("\nEs sind insgesamt " + str(usercount) + " User auf den Gamingservern unterwegs!")
        print(usercount)
