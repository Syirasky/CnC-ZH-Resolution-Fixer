import os.path
import win32api
import getpass
import os

from shutil import copyfile


#for getting screen resolution width and height
width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
print ("Width =", width)
print ("Height =", height)
os.system('color 3')
#get input huhu
print ("CNC General ZH Screen Resolution Fixer by Syirasky")
syr = """
          _____       _               _                   
         /  ___|     (_)             | |                  
 ______  \ `--. _   _ _ _ __ __ _ ___| | ___   _   ______ 
|______|  `--. \ | | | | '__/ _` / __| |/ / | | | |______|
         /\__/ / |_| | | | | (_| \__ \   <| |_| |         
         \____/ \__, |_|_|  \__,_|___/_|\_\\__,  |         
                __/ /                      __/ /         
               |___/                      |___/           """
print(syr)
print("------------------------------------------------------------------------------")
print("[1] Default width,height (1024,768)")
print("[2] Fullscreen to your default screen width,height (%d,%d)"%(width,height))
print("")

print("If you need help, follow me and drop a dm.")


print("#Github  : https://github.com/Syirasky")
print("#Facebook: https://www.facebook.com/ras.rizal.1")
print("#Twitter : https://twitter.com/RasrizalRosdi")
print("#Youtube : https://www.youtube.com/channel/UCFF8e2yV-K-hssD8dlh7HWw")
print("")

print("#Disclaimer: As you proceed, I not responsible if any damage occured happened.")

print("------------------------------------------------------------------------------")

#get username
user= getpass.getuser()
print('Username:',user)

print("Enter Your Choice")


chs = int(input(">"))





config = """AntiAliasing = 1 
BuildingOcclusion = yes
CampaignDifficulty = 0
DrawScrollAnchor =
DynamicLOD = yes
ExtraAnimations = yes
GameSpyIPAddress = 0.0.0.0
Gamma = 50
HeatEffects = yes
IPAddress = 0.0.0.0
IdealStaticGameLOD = Low
LanguageFilter = false
MaxParticleCount = 5000
MoveScrollAnchor =
MusicVolume = 55
Resolution = 1024 768
Retaliation = yes
SFX3DVolume = 79
SFXVolume = 71
ScrollFactor = 59
SendDelay = no
ShowSoftWaterEdge = yes
ShowTrees = yes
StaticGameLOD = High
TextureReduction = 0
UseAlternateMouse = no
UseCloudMap = yes
UseDoubleClickAttackMove = no
UseLightMap = yes
UseShadowDecals = yes
UseShadowVolumes = yes
VoiceVolume = 70
"""


config2 = """AntiAliasing = 1 
BuildingOcclusion = yes
CampaignDifficulty = 0
DrawScrollAnchor =
DynamicLOD = yes
ExtraAnimations = yes
GameSpyIPAddress = 0.0.0.0
Gamma = 50
HeatEffects = yes
IPAddress = 0.0.0.0
IdealStaticGameLOD = Low
LanguageFilter = false
MaxParticleCount = 5000
MoveScrollAnchor =
MusicVolume = 55
Resolution = %d %d
Retaliation = yes
SFX3DVolume = 79
SFXVolume = 71
ScrollFactor = 59
SendDelay = no
ShowSoftWaterEdge = yes
ShowTrees = yes
StaticGameLOD = High
TextureReduction = 0
UseAlternateMouse = no
UseCloudMap = yes
UseDoubleClickAttackMove = no
UseLightMap = yes
UseShadowDecals = yes
UseShadowVolumes = yes
VoiceVolume = 70
"""%(width,height)




filename = 'Options.ini'

pathfile = 'C:\\Users\\'+user+'\\Documents\\CnC Generals ZH ME Data\\'+filename
print('Path:',pathfile)
dst = 'C:\\Users\\'+user+'\\Documents\\CnC Generals ZH ME Data\\Options.ini.bkp'

#file handling
if os.path.exists(pathfile)==True:
        #file write if exist
        if chs==1:                
                print("File Exist\n")
                openedfile = open(pathfile,'w')
                openedfile.write(config)
                openedfile.close()
        else:
                
                print("File Exist\n")
                openedfile = open(pathfile,'w')
                openedfile.write(config2)
                openedfile.close()
        
        copyfile(pathfile, dst)
        print("File found. Done backup as Options.ini.bkp")
              
else:
        if chs==1:
                
                print("New File Created")
                openedfile = open(pathfile,'w')
                openedfile.write(config)
                openedfile.close()
        else:
                
                print("New File Created")
                openedfile = open(pathfile,'w')
                openedfile.write(config2)
                openedfile.close()
                
#file read if exist  
openedfile = open(pathfile,'r')
for line in openedfile:
        print(line)
openedfile.close()


print("Enjoy your game. Thank you for using my simple program :) ")
input("Done. Press Any Key ..")

