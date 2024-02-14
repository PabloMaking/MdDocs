from google.cloud import compute_v1

# Set your GCP project ID and zone
project_id = 'mapfre-dig-esp--dat--pro--8620'
zone = 'europe-west1-b'
instance_name = 'model-venus'

# Create a Compute Engine clieinstan    nt
compute_client = compute_v1.InstancesClient()

# Get the instance information
instance_info = compute_client.get(project=project_id, zone=zone, instance=instance_name)

# Display the instance information
print(f"Instance ID: {instance_info.id}")
print(f"Instance Name: {instance_info.name}")
print(f"Machine Type: {instance_info.machine_type}")
print(f"Status: {instance_info.status}")
print(f"Network Interfaces: {instance_info.network_interfaces}")
# Add more attributes as needed
