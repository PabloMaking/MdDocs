import snakemd
def default_print(rows,mddoc,asset_type):
   ''' with open("default.txt", "a") as f:
        print("default " + asset_type, file=f)
'''
    # print(rows)
    # quit(as)
    #mddoc.add_heading(f"Test: {asset_type}",3)
  ##  for row in rows:
         # print(row['name'])
    ##    mddoc.add_paragraph(f"text demo:  {row['name']}  the assets listed below:\n")
        # print(f"Name: {row['displayName']}")
    # for resource in rows.itertuples():
    #     print("name" + resource.name)
    #     print("project" + resource.project)
    #     print("parentFullResourceName" + resource.parentFullResourceName)
    #     print("parentAssetType" + resource.parentAssetType)
    #     print("organization" + resource.organization)
    #     print("assetType" + resource.assetType)
    #     print("displayName" + resource.displayName)
    #     print("location" + resource.location)
    #     print("createTime" + str(resource.createTime))
    #     print("")

def compute_googleapis_com(resource_grouped,mddoc,asset_type):

    mddoc.add_heading("Compute-GoogleApis")

    rows = {}
    header = {}
    Types = []
    
    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        print(Type)
        rows.setdefault(Type, []) # Inicializa una lista vacía si no existe para ese tipo
        match Type:
            case "Address":
                header[Type] = ["Type", "Name", "Location", "State", "Ip"]
                ip = resource['additionalAttributes']['address']
                row = [Type, resource['displayName'], resource['location'], resource['state'], ip]
                rows[Type].append(row)
            case "Disk":
                header[Type] = ["Type", "Name", "SizeType", "State"]
                bytes = resource['additionalAttributes']['sizeGb']
                row = [Type, resource['displayName'], bytes ,resource['state']]
                rows[Type].append(row)


    Types = list(dict.fromkeys(Types))    
    for asset in Types:
        try:
            mddoc.add_heading(asset, 2)
            mddoc.add_table(header[asset], rows[asset], align=None)
        except Exception as e:
            print("Error:", e, "     Coming Soon...")

    mddoc.dump("documents/" + "ReadAssets")
