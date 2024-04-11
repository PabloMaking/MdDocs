from google.cloud import compute_v1   # pip install --upgrade google-cloud-compute
from google.cloud import functions_v1 # pip install google-cloud-functions
import re
import os
import snakemd
import sys

def default_print(resource_grouped,mddoc,asset_type):

    headers = {
        #"artifactregistry.googleapis.com": "ArtifactRegistry-GoogleApis",
        "apikeys.googleapis.com": "ApiKeys-GoogleApis",
        "bigquery.googleapis.com": "Bigquery-GoogleApis",
        "cloudresourcemanager.googleapis.com": "CloudResourceManager-GoogleApis",
        #"containerregistry.googleapis.com": "ContainerRegistry-GoogleApis",
        #"pubsub.googleapis.com": "PubSub-GoogleApis",
        "cloudresourcemanager.googleapis.com": "CloudResourceManager-GoogleApis",
        "cloudtasks.googleapis.com": "CloudTasks-GoogleApis",
        #"cloudfunctions.googleapis.com": "CloudFunctions-GoogleApis",
        "cloudbilling.googleapis.com": "CloudBilling-GoogleApis",
        "serviceusage.googleapis.com": "ServiceUsage-GoogleApis",
        "storage.googleapis.com": "Storage-GoogleApis",
        "vpcaccess.googleapis.com": "VPC-Access-GoogleApis",
    }
    try:
        heading = headers[asset_type]
    except:
        heading = asset_type
        
    mddoc.add_heading(heading)

    
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

'''def apikeys_googleapis_com(resource_grouped,mddoc):
    mddoc.add_heading("ApiKeys-GoogleApis")
'''

def apps_k8s_io(resource_grouped,mddoc):
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
            if(resource['parentFullResourceName'].split("/")[-1] != "kube-system"):
                row = [resource['displayName'],  resource['location'], resource['labels'], resource['parentFullResourceName'].split("/")[-1]]
                rows[Type].append(row)
        else:
            header[Type] = ["Name", "Location","NameSpaces"]
            if(resource['parentFullResourceName'].split("/")[-1] != "kube-system"):
                row = [resource['displayName'],  resource['location'], resource['parentFullResourceName'].split("/")[-1]]
                rows[Type].append(row)
        #print(resource['additionalAttributes']['dnsName'].rstrip('.'))
    mdoc_add(mddoc, rows, header, Types)

def artifactregistry_googleapis_com(resource_grouped,mddoc):
    
    mddoc.add_heading("ArtifactRegistry-GoogleApis")
    mddoc.add_heading("ContainerRegistry-GoogleApis")

    rows = {}
    header = {}
    Types = []

    for resource in resource_grouped:
        Type = str(resource['assetType']).split('/')[-1]
        Types.append(Type)
        rows.setdefault(Type, [])

        header[Type] = ["Name", "Location"]
        row = [resource['displayName'].rsplit('/', 1)[-1].split('@')[0], resource['location']]
        rows[Type].append(row)
    
    mdoc_add(mddoc, rows, header, Types)

def bigquery_googleapis_com(resource_grouped,mddoc):
    mddoc.add_heading("Bigquery-GoogleApis")
    rows = {}
    header = {}
    Types = []

    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        rows.setdefault(Type, [])
        if(Type=='Table'):
            header[Type] = ["Name", "Location"]
            row = [resource['displayName'],  resource['location']]
            if not (partition_date(row[0])):
                rows[Type].append(row)
        else:
            header[Type] = ["Name", "Location"]
            row = [resource['displayName'],  resource['location']]
            rows[Type].append(row)
    mdoc_add(mddoc, rows, header, Types)

'''def cloudbilling_googleapis_com(resource_grouped,mddoc):
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
    mdoc_add(mddoc, rows, header, Types)'''

def cloudfunctions_googleapis_com(resource_grouped,mddoc,project_id):
    
    mddoc.add_heading("CloudFunctions-GoogleApis")
    #project_id = 'mapfre-dig-esp--dat--pro--8620'
    #project_id = "tecuidamos-esp-dat-pre--7838"
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

                function_full_name = f"projects/{project_id}/locations/{resource['location']}/functions/{resource['displayName']}"
                function = client.get_function(name=function_full_name)
                header[Type]=["Name", "Location", "State", "Runtime", "AvailableMemory(MiB)", "Timeout", "ServiceAccount"]
                row = [resource['displayName'], resource['location'], resource['state'], function.runtime, function.available_memory_mb, function.timeout, function.service_account_email]
                rows[Type].append(row)
    mdoc_add(mddoc, rows, header, Types)

'''def cloudresourcemanager_googleapis_com(resource_grouped,mddoc):
    mddoc.add_heading("CloudResourceManager-GoogleApis")
    all_resources(resource_grouped, mddoc)'''

'''def cloudtasks_googleapis_com(resource_grouped,mddoc):
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
    mdoc_add(mddoc, rows, header, Types)'''

def compute_googleapis_com(resource_grouped,mddoc,project_id):

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
                header[Type] = ["Name", "Location", "State", "IP"]
                ip = resource['additionalAttributes']['address']
                row = [resource['displayName'], resource['location'], resource['state'], ip]
                rows[Type].append(row)

            case "Disk":
                header[Type] = ["Name", "Size", "State", "Type"] 
                row = [resource['displayName'], resource['additionalAttributes']['sizeGb'] ,resource['state'], resource['additionalAttributes']['type']]
                rows[Type].append(row)

            case "Instance":
                header[Type] = ["Name", "id", "MachineType", "Location", "State", "Network-Name", "Subnetwork", "IP-Interna", "Network-Tier", "Network-Type"]
                #resource['additionalAttributes']['id'] "NetworkTags", "NetworkTier", "NetworkType", "SubNetwork", "IP"

                instance_info = compute_client.get(project=project_id, zone=resource['location'], instance=str(resource['displayName']))
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

def container_googleapis_com(resource_grouped,mddoc):
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

def containerregistry_googleapis_com(resource_grouped,mddoc):
    
    mddoc.add_heading("ContainerRegistry-GoogleApis")

    rows = {}
    header = {}
    Types = []

    for resource in resource_grouped:
        Type = str(resource['assetType']).split('/')[-1]
        Types.append(Type)
        rows.setdefault(Type, [])

        header[Type] = ["Name", "Location"]
        row = ["/".join(resource['displayName'].split('/')[-2:]), resource['location']]
        rows[Type].append(row)
    
    mdoc_add(mddoc, rows, header, Types)
    

def dataflow_googleapis_com(resource_grouped,mddoc):
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
            header[Type] = ["Name", "State", "Location"]
        row = [resource['displayName'], resource['state'].split('_')[-1], resource['location']]
        #if(resource['state']!='JOB_STATE_DRAINED'):
        if(resource['state']=="JOB_STATE_RUNNING"):
            rows[Type].append(row)

    mdoc_add(mddoc, rows, header, Types)

def dns_googleapis_com(resource_grouped,mddoc):
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

def iam_googleapis_com(resource_grouped,mddoc):
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
            row = ["/".join(resource['displayName'].split('/')[-4:])]
        #print(resource['additionalAttributes']['includedPermissions'])
        rows[Type].append(row)
    mdoc_add(mddoc, rows, header, Types)

def logging_googleapis_com(resource_grouped,mddoc):
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

def monitoring_googleapis_com(resource_grouped,mddoc):
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

def pubsub_googleapis_com(resource_grouped,mddoc):
    mddoc.add_heading("PubSub-GoogleApis")
        
    rows = {}
    header = {}
    Types = []
    
    for resource in resource_grouped:
        Type = str(resource['assetType']).split("/")[-1]
        Types.append(Type)
        rows.setdefault(Type, []) # Inicializa una lista vacía si no existe para ese tipo

        header[Type] = ["Name", "Location"]
        row = [resource['displayName'].split('/')[-1], resource['location']]
        rows[Type].append(row)

    mdoc_add(mddoc, rows, header, Types)

def rbac_authorization_k8s_io(resource_grouped,mddoc):
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

def redis_googleapis_com(resource_grouped,mddoc):
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
    
def secretmanager_googleapis_com(resource_grouped,mddoc):
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

'''def serviceusage_googleapis_com(resource_grouped,mddoc):
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
    mdoc_add(mddoc, rows, header, Types)'''
    
def sqladmin_googleapis_com(resource_grouped,mddoc):
    mddoc.add_heading("SQL-Admin-GoogleApis")
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
    Types = list(dict.fromkeys(Types))
    for i in range(len(Types) - 1, -1, -1):
        try:
                mddoc.add_heading(Types[i], 2)
                mddoc.add_table(header[Types[i]], rows[Types[i]], align=None)
        except Exception as e:
            print(e)

'''def storage_googleapis_com(resource_grouped,mddoc):
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
    mdoc_add(mddoc, rows, header, Types)'''

'''def vpcaccess_googleapis_com(resource_grouped,mddoc):
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
    mdoc_add(mddoc, rows, header, Types)'''

def mdoc_add(mddoc, rows, header, Types=None):
    Types = list(dict.fromkeys(Types))
    if(len(Types)!=1):
        for i in Types:
            try:
                if(i=="Role"):
                    mddoc.add_heading("CustomRoles", 2)
                else:
                    mddoc.add_heading(i, 2)
                align = [snakemd.Table.Align.CENTER] * len(header[str(Types[0])])
                mddoc.add_table(header[i], rows[i], align=align)
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
            align = [snakemd.Table.Align.CENTER] * len(header[str(Types[0])])
            print(header[str(Types[0])])
            print(align)
            mddoc.add_table(header[str(Types[0])], rows[str(Types[0])], align=align)
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

def partition_date(element):
    """
    Función booleana que evalúa si un elemento cumple con el patrón "word_YYYYMMDD".
    """
    pattern = re.compile(r'\b\w+_\d{8}\b')
    return bool(pattern.match(element))

def make_dirs(project):
    if not os.path.exists('documents'):
        os.makedirs('documents')
    if not os.path.exists('documents/' + project):
        os.makedirs('documents/' + project)
        #os.makedirs('documents/' + project + '/json')
        os.makedirs('documents/' + project + '/md')

def usage(include_first_line=True):
    if include_first_line:
        print("\nUsage:" + sys.argv[0] + "[OPTION]\n")
    print("\t Options:")
    print("\t\t document    --> Generate MD Documentation")
    #print("\t\t spreadsheet --> Generate Spreadsheet asset inventory")
    print("\t\t json        --> Print assets in JSON")
    #print("\t\t file        --> Export to reports to files")
    #print("\t\t summary     --> Print screen summary projects")
    if not include_first_line:
        print("\t\t exit        --> Export to reports to files")