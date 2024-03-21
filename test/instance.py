from google.cloud import compute_v1
from google.cloud import functions_v1
import re

# Set your GCP project ID and zone
#project_id = 'mapfre-dig-esp--dat--pro--8620'
#zone = 'europe-west1-b'
#instance_name = 'model-venus'
project_id = 'tecuidamos-esp--dat--pre--7838'
zone = 'europe-west1-d'
instance_name = 'pre-tc-trans--pubsub-to-p-03210219-vmtv-harness-k4jf'
# Create a Compute Engine clieinstan    nt
compute_client = compute_v1.InstancesClient()

# Get the instance information
instance_info = compute_client.get(project=project_id, zone=zone, instance=instance_name) # .list   .list_referrers
print(instance_info)
interfaces = str(instance_info.network_interfaces)
# Display the instance information
#print(f"Network Interfaces: {instance_info.network_interfaces}")
#print(f"\n----------------\n: {instance_info.network_performance_config}")
# Add more attributes as needed
def compute_interfaces(interfaces):
    pattern = r'(\w+):\s*"([^"]*)"'
# Buscar todas las coincidencias en la cadena
    matches = re.findall(pattern, interfaces)
    diccionario = {}
    for match in matches:
        key = match[0]
        value = match[1]
        if key in diccionario:
            diccionario[key] = [diccionario[key], value]
            '''if isinstance(diccionario[key], list):
            diccionario[key].append(value)
        else:
            diccionario[key] = [diccionario[key], value]'''
        else:
            diccionario[key] = value
    return diccionario

diccionario = compute_interfaces(interfaces)

# Imprimir el diccionario resultante
print(diccionario)
print(diccionario['name'][0])
print(diccionario['name'][1])