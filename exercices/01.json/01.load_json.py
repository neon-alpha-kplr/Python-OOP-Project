# Import des modules nécessaires
import json
import os
from unidecode import unidecode

# Get the directory path of the current Python file
local_path = os.path.dirname(os.path.abspath(__file__))

# Chargement des données JSON à partir du fichier dans un dictionnaire python
json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))

# Il est nécessaire de reconvertir le dictionnaire en chaine de caractères pour le traiter ensuite
json_str = json.dumps(json_data)

# Utilisation de la fonction unidecode pour enlever les accents et autres caractères spéciaux
json_data = unidecode(json_str)

# Conversion de la chaine de caractere JSON à nouveau en dictionnaire Python
# Le dictionnaire python est plus pratique à manipuler que la chaine de caractère car il est structuré
json_dict = json.loads(json_data)

# Imprimons a présent le dictionnaire
print(json.dumps(json_dict, indent=4))
