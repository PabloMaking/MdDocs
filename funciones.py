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
    
    #print(resource_grouped[1]['assetType'])
    header = ["Type", "Name", "DisplayName", "Location", "State", "Ip"]
    rows = [["Tipo", resource_grouped[1]['assetType'], "Disp", "Aqui", "On", "127.0.0.1"],["1","2","3","4","5","6"]]
    mddoc.add_table(header, rows, align=None)
    print(mddoc)
    mddoc.dump("documents/" + "tabla")
    '''for resource in resource_gruoped:
        print(resource)'''


