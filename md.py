import snakemd
import json
import re
import os
from funciones import *

asset_types = []
mddoc = snakemd.new_doc()
f = open('mapfre-dig-pro.json')
dictResponse = json.load(f)
f.close()

for resource in dictResponse:
    asset_types.append(resource['assetType'])
#print(asset_types) Aqui está el número total de recursos

unique_asset_types = sorted(list(dict.fromkeys(asset_types)))
    # Left only the main resource (remove from / to the $) and do it unique
unique_asset_types_family = (list(dict.fromkeys([re.sub(r'/.*$', '', unique_asset_type) for unique_asset_type in unique_asset_types])))
print((unique_asset_types_family))
for asset_type in unique_asset_types_family:
        # print(f" fuera: {asset_type}")
    resource_grouped = []
    for resource in dictResponse:
        if asset_type in resource['assetType']:
            asset_type_replace = asset_type.replace(".","_")
            resource_grouped.append(resource)
            #print("resource" + str(resource['assetType']))
            #print("Gruoped" + str(len(resource_grouped)))
    try:
        exec(f"{asset_type_replace}(resource_grouped,mddoc,asset_type)")
    except:
        default_print(resource_grouped,mddoc,asset_type)
        pass

#mddoc.add_ordered_list(unique_asset_types_family)
       ## Create documents directory
if not os.path.exists('documents'):
    os.makedirs('documents')

    ## Dump snakeMD document
mddoc.dump("documents/" + "local")

print("Exported MD documents")

