from google.cloud import compute_v1

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

    compute_client = compute_v1.InstancesClient()
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
                header[Type] = ["Name", "Location", "State", "Ip"]
                ip = resource['additionalAttributes']['address']
                row = [resource['displayName'], resource['location'], resource['state'], ip]
                print(row)
                rows[Type].append(row)

            case "Disk":
                header[Type] = ["Name", "SizeType", "State"]
                bytes = resource['additionalAttributes']['sizeGb']
                row = [resource['displayName'], bytes ,resource['state']]
                rows[Type].append(row)

            case "Instance":
                header[Type] = ["Name", "id", "MachineType", "Location", "State", "Network"]
                #resource['additionalAttributes']['id'] "NetworkTags", "NetworkTier", "NetworkType", "SubNetwork", "IP"
                instance_info = compute_client.get(project="mapfre-dig-esp--dat--pro--8620", zone=resource['location'], instance=str(resource['displayName']))
                row = [resource['displayName'], instance_info.id, instance_info.machine_type, resource['location'], instance_info.status, instance_info.network_interfaces]
                #print(instance_info)
                rows[Type].append(row)

    Types = list(dict.fromkeys(Types))
    for asset in Types:
        try:
            mddoc.add_heading(asset, 2)
            mddoc.add_table(header[asset], rows[asset], align=None)
        except Exception as e:
            print("Error:", e, "     Coming Soon...")
    mddoc.dump("documents/" + "ReadAssets")


