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
print(f"Network Interfaces: {instance_info.network_interfaces}")
print(f"\n----------------\n: {instance_info.network_performance_config}")
# Add more attributes as needed
