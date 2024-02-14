# MarkDown para accountability de recursos

## Assets types

In this document we can found a detail about the assets that conform this project. In it, we can see a list of all them and a description of every asset type, a list of assets grouped by type and the details of them.

1. apikeys.googleapis.com
2. apps.k8s.io
3. artifactregistry.googleapis.com
4. bigquery.googleapis.com
5. cloudbilling.googleapis.com
6. cloudfunctions.googleapis.com
7. cloudresourcemanager.googleapis.com
8. cloudtasks.googleapis.com
9. compute.googleapis.com
10. container.googleapis.com
11. containerregistry.googleapis.com
12. dataflow.googleapis.com
13. dns.googleapis.com
14. iam.googleapis.com
15. k8s.io
16. logging.googleapis.com
17. monitoring.googleapis.com
18. pubsub.googleapis.com
19. rbac.authorization.k8s.io
20. redis.googleapis.com
21. secretmanager.googleapis.com
22. serviceusage.googleapis.com
23. sqladmin.googleapis.com
24. storage.googleapis.com
25. vpcaccess.googleapis.com

# Compute-GoogleApis

## Address

| Name                                | Location     | State    | Ip            |
| ----------------------------------- | ------------ | -------- | ------------- |
| mapfre-dig-esp--dat--pro            | global       | IN_USE   | 34.110.141.46 |
| mapfre-dig-esp--dat--pro--private   | global       | RESERVED | 10.40.0.0     |
| mapfre-dig-esp--dat--pro--nat-ip--1 | europe-west1 | IN_USE   | 34.76.116.231 |

## BackendBucket

| Name                                       | location |
| ------------------------------------------ | -------- |
| mapfre-dig-esp--dat--pro--lb-default--250d | global   |
| mapfre-dig-esp--dat--pro--mapper--7056     | global   |
| mapfre-dig-esp--dat--pro--mapper-sql--a25f | global   |

## BackendService

| Name                                              | location |
| ------------------------------------------------- | -------- |
| mapfre-dig-esp--dat--pro--nginx-proxy--lb--public | global   |
| autos-price-ranking--call-endpoint--lb            | global   |
| mapfre-dig-esp--dat--pro--nginx-proxy--lb--iap    | global   |

## Disk

| Name                                                 | SizeType | State |
| ---------------------------------------------------- | -------- | ----- |
| mapfre-dig-esp--dat--pro--autos-price-ranking--vm    | 25.0     | READY |
| model-venus-data                                     | 100.0    | READY |
| model-venus-boot                                     | 100.0    | READY |
| gke-mapfre-dig-esp--dat--pr-np-pro-01-1f12a5cc-w4q6  | 50.0     | READY |
| pro-mapfre-dig-trans--pub-08232315-ocbi-harness-4spg | 30.0     | READY |
| gke-mapfre-dig-esp--dat--pr-np-pro-01-e962b67a-st5z  | 50.0     | READY |
| pro-mapfre-dig-trans--pub-08170030-9675-harness-lxqz | 30.0     | READY |
| gke-mapfre-dig-esp--dat--pr-np-pro-01-5626f4d9-tlzp  | 50.0     | READY |

## Firewall

| Name                                               | Location | State   | Tags                                                | CreationTime         |
| -------------------------------------------------- | -------- | ------- | --------------------------------------------------- | -------------------- |
| pro--autos-price-ranking--22-allow                 | global   | ENABLED | ['ssh-without-public-ip']                           | 2022-07-11T11:03:57Z |
| gke-mapfre-dig-esp--dat--pro--gke-0ad091e2-master  | global   | ENABLED | ['gke-mapfre-dig-esp--dat--pro--gke-0ad091e2-node'] | 2022-04-07T09:21:36Z |
| mapfre-dig-esp--dat--pro--eveng-sourcing--fw       | global   | ENABLED | Null                                                | 2022-04-22T10:06:49Z |
| gke-mapfre-dig-esp--dat--pro--gke-0ad091e2-all     | global   | ENABLED | ['gke-mapfre-dig-esp--dat--pro--gke-0ad091e2-node'] | 2022-04-07T09:21:36Z |
| gke-mapfre-dig-esp--dat--pro--gke-0ad091e2-vms     | global   | ENABLED | ['gke-mapfre-dig-esp--dat--pro--gke-0ad091e2-node'] | 2022-04-07T09:21:37Z |
| pro--autos-price-ranking--models-8080-allow-access | global   | ENABLED | ['models-8080-allow']                               | 2022-07-11T11:06:59Z |

## ForwardingRule

| Name                            | location |
| ------------------------------- | -------- |
| mapfre-dig-esp--dat--pro--https | global   |
| mapfre-dig-esp--dat--pro--http  | global   |

## HealthCheck

| Name                                           | location |
| ---------------------------------------------- | -------- |
| mapfre-dig-esp--dat--pro--nginx-proxy--neg--hc | global   |

## Instance

| Name                                              | id                  | MachineType    | Location       | State      | Network        |
| ------------------------------------------------- | ------------------- | -------------- | -------------- | ---------- | -------------- |
| model-venus                                       | 5806558271339922216 | n1-standard-16 | europe-west1-b | TERMINATED | Coming Soon... |
| mapfre-dig-esp--dat--pro--autos-price-ranking--vm | 6458578003896460107 | e2-standard-2  | europe-west1-b | RUNNING    | Coming Soon... |

## InstanceGroup

| Name                                                     | location       |
| -------------------------------------------------------- | -------------- |
| dataflow-pro-mapfre-dig-trans--pub-08232315-ocbi-harness | europe-west1   |
| gke-mapfre-dig-esp--dat--pr-np-pro-01-1f12a5cc-grp       | europe-west1-b |
| gke-mapfre-dig-esp--dat--pr-np-pro-01-e962b67a-grp       | europe-west1-c |
| gke-mapfre-dig-esp--dat--pr-np-pro-01-5626f4d9-grp       | europe-west1-d |

## InstanceGroupManager

| Name                                                     | location       |
| -------------------------------------------------------- | -------------- |
| dataflow-pro-mapfre-dig-trans--pub-08232315-ocbi-harness | europe-west1   |
| dataflow-pro-mapfre-dig-trans--pub-08170030-9675-harness | europe-west1   |
| gke-mapfre-dig-esp--dat--pr-np-pro-01-1f12a5cc-grp       | europe-west1-b |
| gke-mapfre-dig-esp--dat--pr-np-pro-01-e962b67a-grp       | europe-west1-c |
| gke-mapfre-dig-esp--dat--pr-np-pro-01-5626f4d9-grp       | europe-west1-d |

## InstanceTemplate

| Name                                                       | location     |
| ---------------------------------------------------------- | ------------ |
| gke-mapfre-dig-esp--dat--pr-np-pro-01-1f12a5cc             | global       |
| gke-mapfre-dig-esp--dat--pr-np-pro-01-5626f4d9             | global       |
| gke-mapfre-dig-esp--dat--pr-np-pro-01-e962b67a             | global       |
| dataflow-pro-mapfre-dig-trans--pub-08232315-ocbi-harness   | europe-west1 |
| dataflow-pro-mapfre-dig-trans--pub-08170030-9675-harness-1 | europe-west1 |

## Network

| Name                     | location |
| ------------------------ | -------- |
| mapfre-dig-esp--dat--pro | global   |

## NetworkEndpointGroup

| Name                                       | location       |
| ------------------------------------------ | -------------- |
| neg--autos-price-ranking--call-endpoint    | europe-west1   |
| mapfre-dig-esp--dat--pro--nginx-proxy--neg | europe-west1-b |
| mapfre-dig-esp--dat--pro--nginx-proxy--neg | europe-west1-c |
| mapfre-dig-esp--dat--pro--nginx-proxy--neg | europe-west1-d |

## Project

| Name                           | location |
| ------------------------------ | -------- |
| mapfre-dig-esp--dat--pro--8620 | global   |

## Route

| Name | Location | Info | CreationTime |
| ---- | -------- | ---- | ------------ |

## Router

| Name                             | location     |
| -------------------------------- | ------------ |
| mapfre-dig-esp--dat--pro--router | europe-west1 |

## SecurityPolicy

| Name       | location |
| ---------- | -------- |
| white-list | global   |

## SslCertificate

| Name                                  | location |
| ------------------------------------- | -------- |
| mapfre-dig-esp--dat--pro-main--57af   | global   |
| mapfre-dig-esp--dat--pro-models--9514 | global   |

## Subnetwork

| Name                                             | location     |
| ------------------------------------------------ | ------------ |
| mapfre-dig-esp--dat--pro--europe-west1--internal | europe-west1 |

## TargetHttpProxy

| Name                          | location |
| ----------------------------- | -------- |
| mapfre-dig-esp--dat--pro-http | global   |

## TargetHttpsProxy

| Name                           | location |
| ------------------------------ | -------- |
| mapfre-dig-esp--dat--pro-https | global   |

## UrlMap

| Name                            | location |
| ------------------------------- | -------- |
| mapfre-dig-esp--dat--pro--http  | global   |
| mapfre-dig-esp--dat--pro--https | global   |