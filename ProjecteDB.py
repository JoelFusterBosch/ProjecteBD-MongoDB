from pymongo import MongoClient
client = MongoClient('mongodb://admin:admin@localhost:20000/admin?authSource=admin')
db=client['admin']
print(client)
eixir='n'
while eixir=='n':
    canal=input("Vols posar un canal? s/n")
    if(canal=='s'):
        coleccio_canal=db.create_collection('canal')
        Subscripció_activada=bool(input("El usuari té una subscripció?"))
        IDcan=input("Quina és la ID del canal?")
        if(IDcan!="" and Subscripció_activada!=""):
            coleccio_canal.insertOne(f"Subscripció activada",{Subscripció_activada},
                        "ID del canal",{IDcan})
        print(f"coleccio_canal")
    capitol=input("Vols posar un capitol? s/n")
    if (capitol=='s'):
        coleccio_capitol=db.create_collection('capitol')
        IDcap=input("Quina és el ID del capitol?")
        Nomcap=input("Com es diu el captilol")
        Numcap=int(input("Quin número es el capitol?"))
        Durada_del_capitol=int(input("Quant dura el capitol?"))
        if(Durada_del_capitol<0 or Durada_del_capitol>57):
            print("No pot durar més de 0 min o més de 57 min")
        else:
            if(IDcap!="" and  Nomcap!="" and Numcap>0 ):
                coleccio_capitol.insertOne(f"ID del Capitol:",{IDcap},
                                   "Durada del capitol:",{Durada_del_capitol},
                                   "Nom del capitol:",{Nomcap},
                                   "Número del capitol",{Numcap},)
    Programes=input("Vols fer un programa? s/n")
    if(Programes=='s'):
        coleccio_programes=db.create_collection('Programes')
        IDpr=input("Quina és la ID del programa?")
        Rating =int(input("Quin rating té?"))
        Expectativa_de_emisió=int(input("Quants anys pensa estar en emisió?"))
        Genere=input("De quin genere es?")
        Descripció=input("Quina descripció té el programa")
        Edat_general=input("Quina és la edat general")
        Nom_del_programa=input("Com es diu el programa")
        Nºtemp=int(input("Quantes temporades té?"))
        Nºcap=int(input("Quants capitols té?"))
        if(IDpr!="" and Rating!="" and Expectativa_de_emisió>0 and Genere!="" and Edat_general>0 and Nom_del_programa!="" and Nºtemp>3 and Nºcap>20 ):
            coleccio_programes.insertOne(f"ID del programa:",{IDpr},
                                   "Rating:",{Rating},
                                   "Expectativa de emisió",{Expectativa_de_emisió},
                                   "Genere:",{Genere},
                                   "Descripció",{Descripció},
                                   "Edat general",{Edat_general},
                                   "Nom del programa",{Nom_del_programa},
                                   "Número de temporada",{Nºtemp},
                                   "Número del capitol",{Nºcap})
    Propaganda=input("Vols posar un canal? s/n")
    if(Propaganda=='s'):
        coleccio_prop=db.create_collection('canal')
        IDprop=input("Quina és la ID de la propaganda?")
        if(IDprop!=""):
            coleccio_prop.insertOne(f"IDprop:",{IDprop})
    Temporades=input("Vols posar un canal? s/n")
    if(Temporades=='s'):
        coleccio_temp=db.create_collection('canal')
        IDtemp=input("Quina és la ID del canal?")
        Numtemp=int(input("Quantes temporades té?"))
        if(IDtemp!="" and Numtemp>0):
            coleccio_temp.insertOne(f"ID de la temporada:",{IDtemp},","
                                    "Número temporal:",{Numtemp})
    Usuaris=input("Vols posar un usuari? s/n")
    if(Usuaris=='s'):
        coleccio_us=db.create_collection('canal')
        IDus=(input("Quina és la ID del usuari?"))
        Registrarse=bool(input("El usuario esta registrado?"))
        nomUs= input("Quin nom d'usuari vols?")
        Contrasenya=input("Quina contrasenya vols?")
        db.command(f"createUser",{nomUs}, pwd=Contrasenya)
        print("Usuari creat")
        if(IDus!="" and Registrarse!=None):
            coleccio_us.insertOne(f"ID del usuari:",{IDus},
                                     "Registrarse",{Registrarse}) 
    canal=input("Vols eixir ja? s/n")
    MongoClient.close()