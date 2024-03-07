from google.cloud import compute_v1
import re

def default_print(resource_grouped,mddoc,asset_type):
    mddoc.add_heading(asset_type)
    rows = {}
    header = {}
    Types = []
    
    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        rows.setdefault(Type, []) # Inicializa una lista vacía si no existe para ese tipo
        try:
            header[Type] = ["Name", "Location", "State"]
            row = [resource['displayName'], resource['location'], resource['state']]
        except:
            try:
                header[Type] = ["Name", "Location"]
                row = [resource['displayName'], resource['location']]
            except:
                try:
                    header[Type] = ["Name"]
                    row = [resource['displayName']]
                except:
                    pass
        rows[Type].append(row)

    mdoc_add(mddoc, rows, header, Types)

'''def apikeys_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("ApiKeys-GoogleApis")
'''

def apps_k8s_io(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("AppsK8s-GoogleApis")
    rows = {}
    header = {}
    Types = []
    
    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        rows.setdefault(Type, []) # Inicializa una lista vacía si no existe para ese tipo
        if(Type=='ReplicaSet'):
            header[Type] = ["Name", "Location", "Labels","NameSpaces"]
            row = [resource['displayName'],  resource['location'], resource['labels'], resource['parentFullResourceName'].split("/")[-1]]
        else:
            header[Type] = ["Name", "Location","NameSpaces"]
            row = [resource['displayName'],  resource['location'], resource['parentFullResourceName'].split("/")[-1]]
        #print(resource['additionalAttributes']['dnsName'].rstrip('.'))
        rows[Type].append(row)
    mdoc_add(mddoc, rows, header, Types)

'''def artifactregistry_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("ArtifactRegistry-GoogleApis")
    all_resources(resource_grouped, mddoc)'''

'''def bigquery_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("Bigquery-GoogleApis")
    rows = {}
    header = {}
    Types = []

    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        rows.setdefault(Type, [])
        header[Type] = ["Name", "Location"]
        row = [resource['displayName'],  resource['location']]
        #print(resource['additionalAttributes']['dnsName'].rstrip('.'))
        rows[Type].append(row)
    mdoc_add(mddoc, rows, header, Types)'''

def cloudbilling_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("CloudBilling-GoogleApis")
    rows = {}
    header = {}
    Types = []
    
    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        rows.setdefault(Type, []) # Inicializa una lista vacía si no existe para ese tipo
        header[Type] = ["Name", "Location","State"]
        row = [resource['displayName'],  resource['location'],resource['state']]
        #print(resource['additionalAttributes']['dnsName'].rstrip('.'))
        rows[Type].append(row)
    mdoc_add(mddoc, rows, header, Types)

def cloudfunctions_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("CloudFunctions-GoogleApis")
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
            header[Type]=["Name"]
        row.append(resource['displayName'])
        rows[Type].append(row)
    
    mdoc_add(mddoc, rows, header, Types)

'''def cloudresourcemanager_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("CloudResourceManager-GoogleApis")
    all_resources(resource_grouped, mddoc)'''

def cloudtasks_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("CloudTasks-GoogleApis")
    rows = {}
    header = {}
    Types = []
    
    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        rows.setdefault(Type, []) # Inicializa una lista vacía si no existe para ese tipo
        header[Type] = ["Name", "Location", "State"]
        row = [resource['displayName'], resource['location'],resource['state']]
        #print(resource['additionalAttributes']['dnsName'].rstrip('.'))
        rows[Type].append(row)
    mdoc_add(mddoc, rows, header, Types)

def compute_googleapis_com(resource_grouped,mddoc,asset_type):

    mddoc.add_heading("Compute-GoogleApis")

    compute_client = compute_v1.InstancesClient()
    rows = {}
    header = {}
    Types = []
    
    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        #print(Type)
        rows.setdefault(Type, []) # Inicializa una lista vacía si no existe para ese tipo
        
        match Type:
            case "Address":
                header[Type] = ["Name", "Location", "State", "Ip"]
                ip = resource['additionalAttributes']['address']
                row = [resource['displayName'], resource['location'], resource['state'], ip]
                rows[Type].append(row)

            case "Disk":
                header[Type] = ["Name", "Size", "State", "Type"] 
                row = [resource['displayName'], resource['additionalAttributes']['sizeGb'] ,resource['state'], resource['additionalAttributes']['type']]
                rows[Type].append(row)

            case "Instance":
                header[Type] = ["Name", "id", "MachineType", "Location", "State", "Network-Name", "Subnetwork", "IP", "Network-Tier", "Network-Type"]
                #resource['additionalAttributes']['id'] "NetworkTags", "NetworkTier", "NetworkType", "SubNetwork", "IP"

                instance_info = compute_client.get(project="mapfre-dig-esp--dat--pro--8620", zone=resource['location'], instance=str(resource['displayName']))
                machine_type = instance_info.machine_type.split("/")[-1]
                status=instance_info.status
                if(status=="TERMINATED"):
                    status="STOPPED"
                dic_net = compute_interfaces(str(instance_info.network_interfaces))
                try:
                    row = [resource['displayName'], instance_info.id, machine_type, resource['location'], status, dic_net['name'][0], dic_net['subnetwork'].split("/")[-1], dic_net['network_i_p'], dic_net['network_tier'], dic_net['type_']]
                except:
                    row = [resource['displayName'], instance_info.id, machine_type, resource['location'], status, dic_net['name'], dic_net['subnetwork'].split("/")[-1], dic_net['network_i_p'], "Null", "Null"]
                rows[Type].append(row)

            case "Firewall":
                header[Type] = ["Name", "Location", "State", "Tags", "CreationTime"]
                try:
                    tag=resource['networkTags']
                except:
                    tag="Null"
                row = [resource['displayName'], resource['location'], resource['state'], tag, resource['createTime']]
                rows[Type].append(row)

            case "Route":
                header[Type] = ["Name", "Location", "Info", "CreationTime"]
                row = [resource['displayName'], resource['location'], resource['description'], resource['createTime']]
                rows[Type].append(row)

            case "Subnetwork":
                header[Type] = ["Name", "Location", "Gateway-IP"]
                row = [resource['displayName'], resource['location'],resource['additionalAttributes']['gatewayAddress']]
                rows[Type].append(row)

            case _:
                header[Type] = ["Name", "location"]
                row = [resource['displayName'], resource['location']]
                rows[Type].append(row)
    
    mdoc_add(mddoc, rows, header, Types)

def container_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("Container-GoogleApis")
    rows = {}
    header = {}
    Types = []
    
    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        rows.setdefault(Type, []) # Inicializa una lista vacía si no existe para ese tipo
        if(Type=='Cluster'):
            header[Type] = ["Name", "NetworkTags", "Atributes","State"]
            row = [resource['displayName'],  resource['networkTags'], resource['additionalAttributes'], resource['state']]
        else:
            header[Type] = ["Name", "Labels","NetworkTags","Atributes","State"]
            row = [resource['displayName'],  resource['labels'],resource['networkTags'], resource['additionalAttributes'], resource['state']]
        #print(resource['additionalAttributes']['dnsName'].rstrip('.'))
        rows[Type].append(row)

    mdoc_add(mddoc, rows, header, Types)

'''def containerregistry_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("ContainerRegistry-GoogleApis")
    all_resources(resource_grouped, mddoc)'''

def dataflow_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("DataFlow-GoogleApis")
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
            header[Type] = ["Name", "Estado", "Location"]
        row = [resource['displayName'], resource['state'].split('_')[-1], resource['location']]
        if(resource['state']!='JOB_STATE_DRAINED'):
            rows[Type].append(row)

    mdoc_add(mddoc, rows, header, Types)

def dns_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("DNS-GoogleApis")
    rows = {}
    header = {}
    Types = []
    
    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        rows.setdefault(Type, []) # Inicializa una lista vacía si no existe para ese tipo
        header[Type] = ["Name", "Description", "Labels", "Atributos", "State"]
        row = [resource['displayName'],  resource['description'], resource['labels'], resource['additionalAttributes']['dnsName'].rstrip('.'), resource['state']]
        #print(resource['additionalAttributes']['dnsName'].rstrip('.'))
        rows[Type].append(row)
    mdoc_add(mddoc, rows, header, Types)

def iam_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("IAM-GoogleApis")
    rows = {}
    header = {}
    Types = []
    
    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        rows.setdefault(Type, []) # Inicializa una lista vacía si no existe para ese tipo
        if(Type=='Role'):
            header[Type] = ["Name", "Description", "Permisos", "State"]
            row = [resource['displayName'],  resource['description'], resource['additionalAttributes']['includedPermissions'], resource['state']]
        elif(Type=='ServiceAccount'):
            header[Type] = ["Name", "Correo", "State"]
            row = [resource['displayName'].replace("|", "-"),resource['additionalAttributes']['email'], resource['state']]    
        else:
            header[Type] = ["Name"]
            row = [resource['displayName']]
        #print(resource['additionalAttributes']['includedPermissions'])
        rows[Type].append(row)
    mdoc_add(mddoc, rows, header, Types)

def logging_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("Logging-GoogleApis")
    rows = {}
    header = {}
    Types = []
    
    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        rows.setdefault(Type, []) # Inicializa una lista vacía si no existe para ese tipo
        if(Type=='LogBucket'):
            header[Type] = ["Name", "Description", "Location", "State"]
            row = [resource['displayName'].split('/')[-1],  resource['description'], resource['location'], resource['state']]    
        else:
            header[Type] = ["Name", "Desciption", "Location"]
            try:
                row = [resource['displayName'], resource['description'], resource['location']]
            except:
                row = [resource['displayName'], "Null", resource['location']]
        #print(resource['additionalAttributes']['includedPermissions'])
        rows[Type].append(row)
    mdoc_add(mddoc, rows, header, Types)

def monitoring_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("Monitoring-GoogleApis")
    rows = {}
    header = {}
    Types = []
    
    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        rows.setdefault(Type, []) # Inicializa una lista vacía si no existe para ese tipo
        
        header[Type] = ["Name", "Location"]
        row = [resource['displayName'].replace("|", "-"), resource['location']]

        rows[Type].append(row)
    
    mdoc_add(mddoc, rows, header, Types)

'''def pubsub_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("PubSub-GoogleApis")
    all_resources(resource_grouped, mddoc)'''

def rbac_authorization_k8s_io(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("RbacAuthK8S-GoogleApis")
    rows = {}
    header = {}
    Types = []
    
    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        rows.setdefault(Type, []) # Inicializa una lista vacía si no existe para ese tipo
        
        header[Type] = ["Name", "Location", "Labels"]
        try:
            row = [resource['displayName'], resource['location'], resource['labels']]
        except:
            row = [resource['displayName'], resource['location'], "Null"]
        rows[Type].append(row)
    
    mdoc_add(mddoc, rows, header, Types)

def redis_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("Redis-GoogleApis")
    rows = {}
    header = {}
    Types = []
    
    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        rows.setdefault(Type, []) # Inicializa una lista vacía si no existe para ese tipo
        
        header[Type] = ["Name", "Location", "State"]
        row = [resource['name'].split('/')[-1], resource['location'], resource['state']]

        rows[Type].append(row)
    mdoc_add(mddoc, rows, header, Types)
    
def secretmanager_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("SecretManager-GoogleApis")
    rows = {}
    header = {}
    Types = []
    
    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        rows.setdefault(Type, []) # Inicializa una lista vacía si no existe para ese tipo
        if(Type=='Secret'):
            header[Type] = ["Name", "Location", "Labels"]
            try:
                row = [resource['displayName'].split('/')[-1], resource['location'], resource['labels']]
            except:
                row = [resource['displayName'].split('/')[-1], resource['location'], "Null"]
            rows[Type].append(row)
        else:
            pass

    mdoc_add(mddoc, rows, header, Types)

def serviceusage_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("ServiceUsage-GoogleApis")
    rows = {}
    header = {}
    Types = []
    
    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        rows.setdefault(Type, []) # Inicializa una lista vacía si no existe para ese tipo

        header[Type] = ["Name", "Location", "State"]
        row = [resource['displayName'], resource['location'], resource['state']]

        rows[Type].append(row)
    mdoc_add(mddoc, rows, header, Types)
    
def sqladmin_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("SQL-Admin-GoogleApis")
    rows = {}
    header = {}
    Types = []
    
    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        rows.setdefault(Type, []) # Inicializa una lista vacía si no existe para ese tipo

        header[Type] = ["Name", "Location", "State"]
        row = ['/'.join(resource['name'].split('/')[3:]), resource['location'], resource['state']]

        rows[Type].append(row)
    mdoc_add(mddoc, rows, header, Types)

def storage_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("Storage-GoogleApis")
    rows = {}
    header = {}
    Types = []
    
    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        rows.setdefault(Type, []) # Inicializa una lista vacía si no existe para ese tipo

        header[Type] = ["Name", "Location"]
        row = [resource['displayName'], resource['location']]

        rows[Type].append(row)
    mdoc_add(mddoc, rows, header, Types)

def vpcaccess_googleapis_com(resource_grouped,mddoc,asset_type):
    mddoc.add_heading("VPC-Access-GoogleApis")
    rows = {}
    header = {}
    Types = []
    
    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        rows.setdefault(Type, []) # Inicializa una lista vacía si no existe para ese tipo

        header[Type] = ["Name", "Location", "State"]
        row = [resource['displayName'], resource['location'], resource['state']]

        rows[Type].append(row)
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

def compute_interfaces(interfaces):
    pattern = r'(\w+):\s*"([^"]*)"'
    matches = re.findall(pattern, interfaces)
    diccionario = {}
    for match in matches:
        key = match[0]
        value = match[1]
        if key in diccionario:
            diccionario[key] = [diccionario[key], value]
        else:
            diccionario[key] = value
    return diccionario