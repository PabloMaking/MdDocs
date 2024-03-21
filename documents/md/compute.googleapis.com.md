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

| Name                                                 | Size  | State | Type        |
| ---------------------------------------------------- | ----- | ----- | ----------- |
| mapfre-dig-esp--dat--pro--autos-price-ranking--vm    | 25.0  | READY | pd-standard |
| model-venus-data                                     | 100.0 | READY | pd-standard |
| model-venus-boot                                     | 100.0 | READY | pd-standard |
| gke-mapfre-dig-esp--dat--pr-np-pro-01-1f12a5cc-w4q6  | 50.0  | READY | pd-ssd      |
| pro-mapfre-dig-trans--pub-08232315-ocbi-harness-4spg | 30.0  | READY | pd-standard |
| gke-mapfre-dig-esp--dat--pr-np-pro-01-e962b67a-st5z  | 50.0  | READY | pd-ssd      |
| pro-mapfre-dig-trans--pub-08170030-9675-harness-lxqz | 30.0  | READY | pd-standard |
| gke-mapfre-dig-esp--dat--pr-np-pro-01-5626f4d9-tlzp  | 50.0  | READY | pd-ssd      |

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

| Name                                              | id                  | MachineType    | Location       | State   | Network-Name | Subnetwork                                       | IP         | Network-Tier | Network-Type   |
| ------------------------------------------------- | ------------------- | -------------- | -------------- | ------- | ------------ | ------------------------------------------------ | ---------- | ------------ | -------------- |
| model-venus                                       | 5806558271339922216 | n1-standard-16 | europe-west1-b | STOPPED | external-nat | mapfre-dig-esp--dat--pro--europe-west1--internal | 10.31.0.35 | PREMIUM      | ONE_TO_ONE_NAT |
| mapfre-dig-esp--dat--pro--autos-price-ranking--vm | 6458578003896460107 | e2-standard-2  | europe-west1-b | RUNNING | nic0         | mapfre-dig-esp--dat--pro--europe-west1--internal | 10.31.0.26 | Null         | Null           |

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

| Name                           | Location | Info                                                                        | CreationTime         |
| ------------------------------ | -------- | --------------------------------------------------------------------------- | -------------------- |
| default-route-6a375665176728f1 | global   | Default local route to the subnetwork 10.103.16.0/21.                       | 2022-04-07T09:19:09Z |
| default-route-42b54e67e394ef9c | global   | Default route to the Internet.                                              | 2022-04-07T09:18:23Z |
| default-route-0af86dcfba389ef3 | global   | Default local route to the subnetwork 10.31.0.0/16.                         | 2022-04-07T09:18:38Z |
| default-route-73f29100daac9949 | global   | Default local route to the subnetwork 10.103.24.0/25.                       | 2022-04-07T09:19:13Z |
| peering-route-588e3a5a0a9ce37c | global   | Auto generated route via peering [gke-n1f738b7506a0097e937-3d53-59f7-peer]. | 2022-04-07T09:20:33Z |
| peering-route-63e242e6f3bcdd72 | global   | Auto generated route via peering [servicenetworking-googleapis-com].        | 2022-04-07T09:40:22Z |
| default-route-837cb59411699651 | global   | Default local route to the subnetwork 10.8.0.0/28.                          | 2022-04-07T09:18:49Z |
| peering-route-72a743763045fda9 | global   | Auto generated route via peering [redis-peer-76544245151].                  | 2022-04-22T10:08:35Z |

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

| Name                                             | Location     | Gateway-IP |
| ------------------------------------------------ | ------------ | ---------- |
| mapfre-dig-esp--dat--pro--europe-west1--internal | europe-west1 | 10.31.0.1  |

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