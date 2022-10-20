import shutil 
import os 
from os import mkdir
from os import makedirs


################### SABER LOS DIRECTORIOS DE UNA CARPTA EN ESPESIFICO ####################################
with os.scandir() as ficheros:
    subdirectorios = [fichero.name for fichero in ficheros if fichero.is_dir()]


################### CREANDO CARPETAS SI NO ESTAN ECHAS #######################################
try:
    imagenes = subdirectorios.index("Imagenes")
except:
    makedirs("Imagenes")
try:
  documen = subdirectorios.index("Documentos")
except:
  mkdir("Documentos")
  mkdir("./Documentos/Pdf")
  mkdir("./Documentos/Word")
  mkdir("./Documentos/Exel")
  
  
try:
  subdirectorios.index("Videos")
except:
  mkdir("Videos")

############ MOVIENDO LOS ARCHIVOS ##################################

archivos = os.listdir()

for a in archivos: 
    if a.endswith(".jpg") or a.endswith(".png"): 
        shutil.move(a,"Imagenes")
        
for b in archivos: 
    if b.endswith(".pdf"):   
        shutil.move(b,"./Documentos/Pdf")  
        
    elif b.endswith(".docx") or b.endswith(".doc"):
        shutil.move(b,"./Documentos/Word")
        
    elif b.endswith(".xlsx"):
        shutil.move(b,"./Documentos/Exel")

for c in archivos: 
    if c.endswith(".mp4"):
        shutil.move(c,"Videos")         
      
        