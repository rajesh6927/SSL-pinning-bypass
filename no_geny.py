fin = open("ssl_pinning_bypass.py", "rt")
data = fin.read()
data = data.replace('./../', '')
data = data.replace('FLAG2 = \"UNCHANGED\"','FLAG2 = \"CHANGED\"')
data = data.replace("It is adviced to clone the SSL-bypass tool in the \"/genymotion/tools\" directory. If you are not using Genymotion, please use the following command,\"python3 no_geny.py\" and try again","If you want to use this with genymotion, run the command, \" python3 with_geny.py\"")
fin.close()
fin = open("ssl_pinning_bypass.py", "wt")
fin.write(data)
fin.close()
