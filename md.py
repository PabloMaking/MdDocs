import snakemd
import json
import re
import os
from funciones import *


asset_types = []
mddoc = snakemd.new_doc()
ruta = os.path.join('documents', 'mapfre-dig-pro.json')
f = open(ruta)
dictResponse = json.load(f)
f.close()

for resource in dictResponse:
    asset_types.append(resource['assetType'])
#print(asset_types) Aqui está el número total de recursos
unique_asset_types = sorted(list(dict.fromkeys(asset_types)))
unique_asset_types_family = (list(dict.fromkeys([re.sub(r'/.*$', '', unique_asset_type) for unique_asset_type in unique_asset_types])))

mddoc.add_heading("MarkDown para accountability de recursos")
mddoc.add_heading("Assets types", 2)
mddoc.add_paragraph("""In this document we can found a detail about the assets that conform this project. In it, we can see a list of all them and a description of every asset type, a list of assets grouped by type and the details of them.""")
mddoc.add_ordered_list(unique_asset_types_family)
mddoc.dump("Introducción")

if not os.path.exists('documents'):
    os.makedirs('documents')

for asset_type in unique_asset_types_family:
    resource_grouped = []
    for resource in dictResponse:
        if asset_type in resource['assetType']:
            asset_type_replace = asset_type.replace(".","_")
            resource_grouped.append(resource)
    try:
        mddoc = snakemd.new_doc()
        exec(f"{asset_type_replace}(resource_grouped,mddoc,asset_type)")
        mddoc.dump("./documents/md/"+asset_type)
    except:
        mddoc = snakemd.new_doc()
        default_print(resource_grouped,mddoc,asset_type)
        #mddoc.dump("./documents/md/default-"+asset_type)
        mddoc.dump("./documents/md/"+asset_type)
        pass

print("Exported MD documents")

