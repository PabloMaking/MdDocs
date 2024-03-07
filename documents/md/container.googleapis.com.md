# Container-GoogleApis

## Cluster

| Name                          | NetworkTags                                                                                       | Atributes                     | State   |
| ----------------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------- | ------- |
| mapfre-dig-esp--dat--pro--gke | ['europe-west1', 'gke-cluster', 'mapfre-dig-esp--dat--pro--gke', 'n1-standard-4', 'np-01', 'pro'] | {'endpoint': '34.79.109.166'} | RUNNING |

## NodePool

| Name      | Labels                                                                                                                         | NetworkTags                                                                                       | Atributes                                                             | State   |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ------- |
| np-pro-01 | {'cluster': 'mapfre-dig-esp--dat--pro--gke', 'np': '01', 'env': 'pro', 'location': 'europe-west1', 'machine': 'n1-standard-4'} | ['europe-west1', 'gke-cluster', 'mapfre-dig-esp--dat--pro--gke', 'n1-standard-4', 'np-01', 'pro'] | {'locations': ['europe-west1-b', 'europe-west1-c', 'europe-west1-d']} | RUNNING |