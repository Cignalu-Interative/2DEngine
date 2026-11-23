import os
import re

# ---------------- A MODIFIER ----------------
# Chemins relatifs a l'emplacement de ce script (dossier bin)
VCXPROJ_FILES = [
    "../ide/2DPendentLib/2DPendentLib.vcxproj",
    "../ide/2DPendentEngine/2DPendentEngine.vcxproj",
    "../ide/Game/Game.vcxproj",
]

# Ensemble d'outils de plateforme a utiliser (v143 -> v145)
TOOLSET = "v145"
# --------------------------------------------

script_dir = os.path.dirname(os.path.abspath(__file__))

for vcxproj_file in VCXPROJ_FILES:
    vcxproj_path = os.path.normpath(os.path.join(script_dir, vcxproj_file))

    if not os.path.isfile(vcxproj_path):
        print("Fichier introuvable :", vcxproj_path)
        continue

    # Lecture/ecriture en binaire : garde le BOM et les fins de ligne tels quels
    with open(vcxproj_path, "rb") as f:
        content = f.read().decode("utf-8")

    pattern = r"<PlatformToolset>.*?</PlatformToolset>"
    new_tag = "<PlatformToolset>" + TOOLSET + "</PlatformToolset>"
    new_content, count = re.subn(pattern, lambda m: new_tag, content)

    if count == 0:
        print("Aucune balise <PlatformToolset> dans :", vcxproj_path)
    else:
        with open(vcxproj_path, "wb") as f:
            f.write(new_content.encode("utf-8"))
        print(os.path.basename(vcxproj_path), ":", count, "balise(s) modifiee(s) ->", TOOLSET)

# Ensemble d'outils de plateforme a utiliser (v143 -> v145)
TOOLSET = "v145"
# --------------------------------------------

script_dir = os.path.dirname(os.path.abspath(__file__))

for vcxproj_file in VCXPROJ_FILES:
    vcxproj_path = os.path.normpath(os.path.join(script_dir, vcxproj_file))

    if not os.path.isfile(vcxproj_path):
        print("Fichier introuvable :", vcxproj_path)
        continue

    # Lecture/ecriture en binaire : garde le BOM et les fins de ligne tels quels
    with open(vcxproj_path, "rb") as f:
        content = f.read().decode("utf-8")

    pattern = r"<PlatformToolset>.*?</PlatformToolset>"
    new_tag = "<PlatformToolset>" + TOOLSET + "</PlatformToolset>"
    new_content, count = re.subn(pattern, lambda m: new_tag, content)

    if count == 0:
        print("Aucune balise <PlatformToolset> dans :", vcxproj_path)
    else:
        with open(vcxproj_path, "wb") as f:
            f.write(new_content.encode("utf-8"))
        print(os.path.basename(vcxproj_path), ":", count, "balise(s) modifiee(s) ->", TOOLSET)
