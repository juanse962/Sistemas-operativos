def main():
  with open("disk2s1.dmg", "rb") as f:
    data = f.read()

  #Guardamos la data de la imagen en una lista

  mapa = list(map(bin, bytearray(data)))
  longitud = str(len(mapa))
  
  jmpboot = str(bytesToString(mapa[0:3][::-1]))

  bs_OEMName = str(bytesToText(mapa[3:11][::-1]))

  bPB_BytsPerSec = str(bytesToString(mapa[11:13][::-1]))

  bPB_SecPerClus = str(bytesToString(mapa[13:14][::-1]))

  bPB_RsvdSecCnt = str(bytesToString(mapa[14:16][::-1]))

  bPB_NumFATs = str(bytesToString(mapa[16:17][::-1]))

  bPB_RootEntCnt = str(bytesToString(mapa[17:19][::-1]))

  bPB_TotSec16 = str(bytesToString(mapa[19:21][::-1]))

  bPB_Media = str(bytesToString(mapa[21:22][::-1]))

  bPB_FATSz16 = str(bytesToString(mapa[22:24][::-1]))

  bPB_SecPerTrk = str(bytesToString(mapa[24:26][::-1]))

  bPB_NumHeads = str(bytesToString(mapa[26:28][::-1]))

  bPB_HiddSec = str(bytesToString(mapa[28:32][::-1]))

  bPB_TotSec32 = str(bytesToString(mapa[32:36][::-1]))

  bPB_FATSz32 = str(bytesToString(mapa[36:40][::-1]))

  bPB_ExtFlags = str(bytesToString(mapa[40:42][::-1]))

  bPB_BPB_FSVer = str(bytesToString(mapa[42:44][::-1]))

  bPB_RootClus = str(bytesToString(mapa[44:48][::-1]))

  bPB_FSInfo = str(bytesToString(mapa[48:50][::-1]))

  bPB_BkBootSec = str(bytesToString(mapa[50:52][::-1]))

  bPB_Reserved = str(bytesToString(mapa[52:64][::-1]))

  bS_DrvNum = str(bytesToString(mapa[64:65][::-1]))

  bS_Reserved1 = str(bytesToString(mapa[65:66][::-1]))

  bS_BootSig = str(bytesToString(mapa[66:67][::-1]))

  bS_VolID = str(bytesToString(mapa[67:71][::-1]))

  bS_VolLab = str(bytesToText(mapa[71:82][::-1]))

  bS_FilSysType = str(bytesToText(mapa[82:90][::-1]))


  #Estructura de la FAT32

  print("------------------FAT32------------------")
  print("El tamaño de la cadena es: "+longitud)
  print("BS_jmpBoot: " + '0x' + jmpboot)
  print("BS_OEMName: " + bs_OEMName)
  print("BPB_BytsPerSec: " + str(int(bPB_BytsPerSec, 16)))
  print("BPB_SecPerClus: " + str(int(bPB_SecPerClus, 16)))
  print("BPB_RsvdSecCnt: " + str(int(bPB_RsvdSecCnt, 16)))
  print("BPB_NumFATs: " + str(int(bPB_NumFATs, 16)))
  print("BPB_RootEntCnt: " + str(int(bPB_RootEntCnt, 16)))
  print("BPB_TotSec16: " + str(int(bPB_TotSec16, 16)))
  print("BPB_Media: " + bPB_Media)
  print("BPB_FATSz16: " + str(int(bPB_FATSz16, 16)))
  print("BPB_SecPerTrk: " + str(int(bPB_SecPerTrk, 16)))
  print("BPB_NumHeads: " + str(int(bPB_NumHeads, 16)))
  print("BPB_HiddSec: " + str(int(bPB_HiddSec, 16)))
  print("BPB_TotSec32: " + str(int(bPB_TotSec32, 16)))
  print("BPB_FATSz32: " + str(int(bPB_FATSz32, 16)))
  print("BPB_ExtFlags: " + bPB_ExtFlags)
  print("BPB_BPB_FSVer: " + bPB_BPB_FSVer)
  print("BPB_RootClus: " + str(int(bPB_RootClus, 16)))
  print("BPB_FSInfo: " + bPB_FSInfo)
  print("BPB_BkBootSec: " + bPB_BkBootSec)
  print("BPB_Reserved: " + bPB_Reserved)
  print("BS_DrvNum: " + bS_DrvNum)
  print("BS_Reserved1: " + bS_Reserved1)
  print("BS_BootSig: " + bS_BootSig)
  print("BS_VolID: " + bS_VolID)
  print("BS_VolLab: " + bS_VolLab)
  print("BS_FilSysType: " + bS_FilSysType)

  print("-----------------------------------------")
  print("Archivos:")

  rootDirectory=(int(bPB_RsvdSecCnt,16)*int(bPB_BytsPerSec,16))+(int(bPB_NumFATs,16)*int(bPB_FATSz32,16)*int(bPB_BytsPerSec,16))+32
  isLong=hex(int(mapa[rootDirectory+11][2:],2))[2:]+hex(int(mapa[rootDirectory+12][2:],2))[2:]
  #print (hex(int(mapa[rootDirectory][2:],2))[2:])

  while(hex(int(mapa[rootDirectory][2:],2))[2:]!="c"):
    #print ("direccion: "+hex(int(mapa[rootDirectory][2:],2)))

    #isLong
    if(hex(int(mapa[rootDirectory+11][2:],2))[2:]+hex(int(mapa[rootDirectory+12][2:],2))[2:]=="f0"):
      #print("long")
      cuantos=0
      nombre=""
      aux2=rootDirectory
      #print ("hex aux2: " + str(hex(aux2)))
      while(hex(int(mapa[aux2+11][2:],2))[2:]=="f"):
        cuantos=cuantos+1
        aux2=aux2+32
      cuantos=cuantos+1
      #print ("cuantos: " + str(cuantos))
      dondeEmpieza=cuantos-2
      #print ("donde empieza: " + str(dondeEmpieza))
      while(dondeEmpieza>=0):
        for i in range (1,10):
          character = chr(int(mapa[rootDirectory+(dondeEmpieza*32)+i][2:],2))
          #if(character!=chr(255)):
          nombre=nombre+character
        for i in range (14,25):
          character = chr(int(mapa[rootDirectory+(dondeEmpieza*32)+i][2:],2))
          #if(character!=chr(255)):
          nombre=nombre+character
        for i in range (28,32):
          character = chr(int(mapa[rootDirectory+(dondeEmpieza*32)+i][2:],2))
          #if(character!=chr(255)):
          nombre=nombre+character
        dondeEmpieza=dondeEmpieza-1
      nombre = nombre.strip('ÿ')
      print(nombre)
      rootDirectory=rootDirectory+(32*cuantos)
    else:
      #print("no soy long")
      rootDirectory=rootDirectory+32
  

 
  # if hex(mapa[rootDirectory][2:]) == 000f:


#Conversion de bytes a Hexadecimal

def bytesToString(bytes):
  return ''.join([formatHex(hex(int(b, 2))) for b in bytes])

def bytesToText(bytes):
  return ''.join([chr(int(formatHex(hex(int(b, 2))), 16)) for b in bytes[::-1]])

#Formato hexadecimal
def formatHex(hx):
  return hx[2:].zfill(2).upper() 

main()


