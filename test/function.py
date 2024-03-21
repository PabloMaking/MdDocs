from google.cloud import functions_v1





# Get the instance information
project_id = "tecuidamos-esp--dat--pre--7838"
location = 'europe-west1'
function_name = 'anonimize'

client = functions_v1.CloudFunctionsServiceClient()
function_full_name = f"projects/{project_id}/locations/{location}/functions/{function_name}"
function = client.get_function(name=function_full_name)
print(function)
print(function.runtime)
print(function.available_memory_mb)
print(function.timeout)
print(function.service_account_email)