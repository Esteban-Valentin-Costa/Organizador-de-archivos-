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
    mkdir("Imagenes")
   


try:
  documen = subdirectorios.index("Documentos")
except:
  mkdir("Documentos")
  mkdir("./Documentos/Pdf")
  mkdir("./Documentos/Word")
  mkdir("./Documentos/Exel")
  mkdir("./Documentos/Powerpoint")
  
  
try:
  subdirectorios.index("Videos")
except:
  mkdir("Videos")


try:
  archivos_zip = subdirectorios.index("Zip")
except:
  mkdir("Zip")

try:
  archivos_Exe = subdirectorios.index("Aplicaciones")
except:
  mkdir("Aplicaciones")



############ MOVIENDO LOS ARCHIVOS ##################################

archivos = os.listdir()

for a in archivos: 
    if a.endswith(".jpg") or a.endswith(".png") or a.endswith("jpeg") or a.endswith(".gif"): 
        shutil.move(a,"Imagenes")

        
for b in archivos: 
    if b.endswith(".pdf") or b.endswith("PDF"):   
        shutil.move(b,"./Documentos/Pdf")  
        
    elif b.endswith(".docx") or b.endswith(".doc"):
        shutil.move(b,"./Documentos/Word")
        
    elif b.endswith(".xlsx") or b.endswith(".xlsm"):
        shutil.move(b,"./Documentos/Exel")
    
    elif b.endswith(".pptx"):
        shutil.move(b,"./Documentos/Powerpoint")


for c in archivos: 
    if c.endswith(".mp4"):
        shutil.move(c,"Videos")         
      
for e in archivos: 
    if e.endswith(".exe"):
        shutil.move(e,"Aplicaciones")  

for d in archivos: 
    if d.endswith(".zip"):
        shutil.move(d,"Zip")     

   
       

