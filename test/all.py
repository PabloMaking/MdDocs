import snakemd
import json
import re
import os
from google.cloud import functions_v1



def cloudfunctions_googleapis_com(resource_grouped,mddoc):
    
    mddoc.add_heading("CloudFunctions-GoogleApis")

    project_id = 'mapfre-dig-esp--dat--pro--8620'
    client = functions_v1.CloudFunctionsServiceClient()
    rows = {}
    header = {}
    Types = []

    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        rows.setdefault(Type, [])
  
        match Type:
            case "CloudFunction":
                client = functions_v1.CloudFunctionsServiceClient()
                function_full_name = f"projects/{project_id}/locations/{resource['location']}/functions/{resource['displayName']}"
                function = client.get_function(name=function_full_name)
                print(function)
                header[Type]=["Name", "Location", "State", "Runtime", "AvailableMemory", "Timeout", "ServiceAccount"]
                row = [resource['displayName'], resource['location'], resource['state'], function.runtime, function.available_memory_mb, function.timeout, function.service_account_email]
                rows[Type].append(row)
        #function.runtime
        
    
    mdoc_add(mddoc, rows, header, Types)

def mdoc_add(mddoc, rows, header, Types=None):
    Types = list(dict.fromkeys(Types))
    if(len(Types)!=1):
        for i in Types:
            try:
                mddoc.add_heading(i, 2)
                mddoc.add_table(header[i], rows[i], align=None)
            except Exception as e:
                if(i=="Dataset"):
                        header[i].insert(4, "Description")
                        header[i].insert(6, "Creator")
                        for line in rows[i]:
                            while len(line) < 12:
                                if(len(line)==10):
                                    line.insert(4, None)
                                    line.insert(6, None)
                                else:
                                    line.insert(6, None)
    else:
        mddoc.add_heading(str(Types[0]), 2)
        try:
            mddoc.add_table(header[str(Types[0])], rows[str(Types[0])], align=None)
        except Exception as e:
            print(e)

def all_resources(resource_grouped, mddoc):
    rows = {}
    header = {}
    Types = []

    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        row = []
        if Type not in header:
            header[Type] = [] 
            rows[Type] = []
            for item in resource:
                #print(item)
                #print(resource.keys())
                header[Type].append(item)
        for item in resource:
            row.append(resource[item])
        rows[Type].append(row)
    Types = list(dict.fromkeys(Types))
    for i in Types:
        try:
            mddoc.add_heading(i, 2)
            mddoc.add_table(header[i], rows[i], align=None)
        except Exception as e:
            if(i=="Dataset"):
                    header[i].insert(4, "Description")
                    header[i].insert(6, "Creator")
                    for line in rows[i]:
                        while len(line) < 12:
                            if(len(line)==10):
                                line.insert(4, None)
                                line.insert(6, None)
                            else:
                                line.insert(6, None)
            
            if(i=="Function"):
                header[i].insert(6, "labels")
                for line in rows[i]:
                    while len(line) < 12:
                                line.insert(6, None)

            if(i=="CloudFunction"): #Posible fallo
                for line in rows[i]:
                    while len(line) < 13:
                        if(len(line)==11):
                            line.insert(6, None)
                            line.insert(7, None)
                        else:
                            try:
                                desc = line['description']
                                line.insert(6, None)
                            except:
                                line.insert(4,None)

            if(i=="LogSink"):
                header[i].insert(4, "Description")
                header[i].insert(6, "CreateTime")
                header[i].insert(7, "Updatetime")
                for line in rows[i]:
                    while len(line) < 11:
                        line.insert(4,None)
                        line.insert(7,None)
                        line.insert(6,None)
            
            if(i=="AlertPolicy"):
                header[i].insert(4, "Description")
                for line in rows[i]:
                    while len(line) < 11:
                        line.insert(4,None)  #se genera columna de más por nombre              

            if(i=="Secret"):
                for line in rows[i]:
                    while len(line) < 10:
                        line.insert(5,None)

            if i=="ClusterRole" or i=="ClusterRoleBinding" or i=="Role" or i=="RoleBinding" or i=="Service":
                for line in rows[i]:
                    while len(line) < 10:
                        line.insert(5,None)

            

            try:
                mddoc.add_table(header[i], rows[i], align=None)
            except:
                print("Error:", e, "     Coming Soon...")

def apikeys_googleapis_com(resource_grouped,mddoc,asset_type):
    
    mddoc.add_heading("ApiKeys-GoogleApis")
    rows = {}
    header = {}
    #Types = []
    
    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        #Types.append(Type)
        rows.setdefault(Type, []) # Inicializa una lista vacía si no existe para ese tipo
        header[Type] = ["Name", "CreationTime", "UpdateTime"]
        row = [resource['displayName'],  resource['createTime'], resource['updateTime']]
        rows[Type].append(row)
    mddoc.add_heading(Type, 2)
    mddoc.add_table(header[Type], rows[Type], align=None)
    
    Types = list(dict.fromkeys(Types))
    for asset in Types:
        try:
            mddoc.add_heading(asset, 2)
            mddoc.add_table(header[asset], rows[asset], align=None)
        except Exception as e:
            print("Error:", e, "     Coming Soon...")

asset_types = []
mddoc = snakemd.new_doc()
f = open('/home/makingscience/Escritorio/ms_assets_inventory/mdDocs/test/functions.json')
dictResponse = json.load(f)
f.close()

for resource in dictResponse:
    asset_types.append(resource['assetType'])
#print(asset_types) Aqui está el número total de recursos

unique_asset_types = sorted(list(dict.fromkeys(asset_types)))
    # Left only the main resource (remove from / to the $) and do it unique
unique_asset_types_family = (list(dict.fromkeys([re.sub(r'/.*$', '', unique_asset_type) for unique_asset_type in unique_asset_types])))

for asset_type in unique_asset_types_family:
    resource_grouped = []
    for resource in dictResponse:
        if asset_type in resource['assetType']:
            asset_type_replace = asset_type.replace(".","_")
            resource_grouped.append(resource)
    try:
        if(asset_type=="cloudfunctions.googleapis.com"):
            cloudfunctions_googleapis_com(resource_grouped,mddoc)
    except Exception as e:
        print("Error:", e, "     Coming Soon...")
mddoc.dump("ALL")
print("Exported MD documents")