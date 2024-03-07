# AppsK8s-GoogleApis

## Deployment

| Name                                      | Location     | NameSpaces                          |
| ----------------------------------------- | ------------ | ----------------------------------- |
| event-exporter-gke                        | europe-west1 | kube-system                         |
| kube-dns                                  | europe-west1 | kube-system                         |
| kube-dns-autoscaler                       | europe-west1 | kube-system                         |
| l7-default-backend                        | europe-west1 | kube-system                         |
| metrics-server-v0.5.2                     | europe-west1 | kube-system                         |
| mapfre-dig-esp--dat--pro--django-consumer | europe-west1 | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer | europe-west1 | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--nginx-proxy     | europe-west1 | mapfre-dig-esp--dat--event-sourcing |

## ReplicaSet

| Name                                                 | Location     | Labels                                                                                  | NameSpaces                          |
| ---------------------------------------------------- | ------------ | --------------------------------------------------------------------------------------- | ----------------------------------- |
| event-exporter-gke-5479fd58c8                        | europe-west1 | {'version': 'v0.3.5', 'k8s-app': 'event-exporter', 'pod-template-hash': '5479fd58c8'}   | kube-system                         |
| event-exporter-gke-67986489c8                        | europe-west1 | {'version': 'v0.3.4', 'k8s-app': 'event-exporter', 'pod-template-hash': '67986489c8'}   | kube-system                         |
| event-exporter-gke-f66d9f855                         | europe-west1 | {'version': 'v0.3.9', 'k8s-app': 'event-exporter', 'pod-template-hash': 'f66d9f855'}    | kube-system                         |
| kube-dns-6554b8577f                                  | europe-west1 | {'k8s-app': 'kube-dns', 'pod-template-hash': '6554b8577f'}                              | kube-system                         |
| kube-dns-697dc8fc8b                                  | europe-west1 | {'k8s-app': 'kube-dns', 'pod-template-hash': '697dc8fc8b'}                              | kube-system                         |
| kube-dns-698cf6b7dc                                  | europe-west1 | {'k8s-app': 'kube-dns', 'pod-template-hash': '698cf6b7dc'}                              | kube-system                         |
| kube-dns-6ffbbcc66d                                  | europe-west1 | {'k8s-app': 'kube-dns', 'pod-template-hash': '6ffbbcc66d'}                              | kube-system                         |
| kube-dns-798f8cc6fb                                  | europe-west1 | {'k8s-app': 'kube-dns', 'pod-template-hash': '798f8cc6fb'}                              | kube-system                         |
| kube-dns-85df8994db                                  | europe-west1 | {'k8s-app': 'kube-dns', 'pod-template-hash': '85df8994db'}                              | kube-system                         |
| kube-dns-autoscaler-844c9d9448                       | europe-west1 | {'k8s-app': 'kube-dns-autoscaler', 'pod-template-hash': '844c9d9448'}                   | kube-system                         |
| kube-dns-autoscaler-f4d55555                         | europe-west1 | {'k8s-app': 'kube-dns-autoscaler', 'pod-template-hash': 'f4d55555'}                     | kube-system                         |
| kube-dns-autoscaler-fbc66b884                        | europe-west1 | {'k8s-app': 'kube-dns-autoscaler', 'pod-template-hash': 'fbc66b884'}                    | kube-system                         |
| kube-dns-b99c7865d                                   | europe-west1 | {'k8s-app': 'kube-dns', 'pod-template-hash': 'b99c7865d'}                               | kube-system                         |
| l7-default-backend-5465dfc4ff                        | europe-west1 | {'k8s-app': 'glbc', 'pod-template-hash': '5465dfc4ff', 'name': 'glbc'}                  | kube-system                         |
| l7-default-backend-56cb9644f6                        | europe-west1 | {'k8s-app': 'glbc', 'pod-template-hash': '56cb9644f6', 'name': 'glbc'}                  | kube-system                         |
| l7-default-backend-58fd4695c8                        | europe-west1 | {'k8s-app': 'glbc', 'pod-template-hash': '58fd4695c8', 'name': 'glbc'}                  | kube-system                         |
| l7-default-backend-69fb9fd9f9                        | europe-west1 | {'k8s-app': 'glbc', 'pod-template-hash': '69fb9fd9f9', 'name': 'glbc'}                  | kube-system                         |
| l7-default-backend-6b99559c7d                        | europe-west1 | {'k8s-app': 'glbc', 'pod-template-hash': '6b99559c7d', 'name': 'glbc'}                  | kube-system                         |
| l7-default-backend-6dc845c45d                        | europe-west1 | {'k8s-app': 'glbc', 'pod-template-hash': '6dc845c45d', 'name': 'glbc'}                  | kube-system                         |
| l7-default-backend-7dc577646d                        | europe-west1 | {'k8s-app': 'glbc', 'pod-template-hash': '7dc577646d', 'name': 'glbc'}                  | kube-system                         |
| metrics-server-v0.5.2-6bf845b67f                     | europe-west1 | {'version': 'v0.5.2', 'k8s-app': 'metrics-server', 'pod-template-hash': '6bf845b67f'}   | kube-system                         |
| metrics-server-v0.5.2-7945948f4b                     | europe-west1 | {'version': 'v0.5.2', 'k8s-app': 'metrics-server', 'pod-template-hash': '7945948f4b'}   | kube-system                         |
| metrics-server-v0.5.2-866bc7fbf8                     | europe-west1 | {'version': 'v0.5.2', 'k8s-app': 'metrics-server', 'pod-template-hash': '866bc7fbf8'}   | kube-system                         |
| mapfre-dig-esp--dat--pro--django-consumer-56f996b5bb | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-consumer', 'pod-template-hash': '56f996b5bb'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-consumer-7bc9b7c674 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-consumer', 'pod-template-hash': '7bc9b7c674'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-54755bfcbf | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '54755bfcbf'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-54f54f4987 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '54f54f4987'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-55b76b8d4c | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '55b76b8d4c'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-56f9668df9 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '56f9668df9'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-5756db487c | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '5756db487c'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-57fc575db9 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '57fc575db9'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-58964547b6 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '58964547b6'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-59449c74d8 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '59449c74d8'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-594779895  | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '594779895'}  | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-5995dd776c | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '5995dd776c'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-5c6bcf4546 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '5c6bcf4546'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-5c6d45cfd6 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '5c6d45cfd6'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-5c7557b4f5 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '5c7557b4f5'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-5cb4db4476 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '5cb4db4476'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-5d9ffb7796 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '5d9ffb7796'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-5f5b98846d | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '5f5b98846d'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-5ff544c7c4 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '5ff544c7c4'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-655b447dbb | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '655b447dbb'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-657f465448 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '657f465448'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-6596c8b8f6 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '6596c8b8f6'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-65b7bd9fcc | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '65b7bd9fcc'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-65fb75d967 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '65fb75d967'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-66c5b849bf | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '66c5b849bf'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-6787cdd48c | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '6787cdd48c'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-6787f77c5f | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '6787f77c5f'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-67b498b848 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '67b498b848'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-67c6fd4fc4 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '67c6fd4fc4'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-685b9f47b9 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '685b9f47b9'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-6889c84984 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '6889c84984'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-6c9565d868 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '6c9565d868'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-6d8bdc89   | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '6d8bdc89'}   | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-6ff75fcfbb | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '6ff75fcfbb'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-74ffbbc84d | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '74ffbbc84d'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-76bc7d78cc | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '76bc7d78cc'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-7759b85988 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '7759b85988'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-77d7bd496b | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '77d7bd496b'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-77dd74b8bb | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '77dd74b8bb'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-7896c74fc8 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '7896c74fc8'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-797658668d | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '797658668d'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-7cffdc5954 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '7cffdc5954'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-7d5dc4fd85 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '7d5dc4fd85'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-7f4b6cc6d7 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '7f4b6cc6d7'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-7f8b9757ff | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '7f8b9757ff'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-847d677798 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '847d677798'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-86cd97fcf5 | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '86cd97fcf5'} | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-8d577cd48  | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': '8d577cd48'}  | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-b9dc67d8   | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': 'b9dc67d8'}   | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-cb6bcc485  | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': 'cb6bcc485'}  | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-cbc5d89b9  | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': 'cbc5d89b9'}  | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-f4f8cd795  | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': 'f4f8cd795'}  | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-f797d9657  | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': 'f797d9657'}  | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-f7ff48b6d  | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': 'f7ff48b6d'}  | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--django-producer-fdc95c8f5  | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--django-producer', 'pod-template-hash': 'fdc95c8f5'}  | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--nginx-proxy-569bcb674      | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--nginx-proxy', 'pod-template-hash': '569bcb674'}      | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--nginx-proxy-5894b457b6     | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--nginx-proxy', 'pod-template-hash': '5894b457b6'}     | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--nginx-proxy-65f4c54bdb     | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--nginx-proxy', 'pod-template-hash': '65f4c54bdb'}     | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--nginx-proxy-665dd5df54     | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--nginx-proxy', 'pod-template-hash': '665dd5df54'}     | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--nginx-proxy-68879f8ffc     | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--nginx-proxy', 'pod-template-hash': '68879f8ffc'}     | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--nginx-proxy-747877d66d     | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--nginx-proxy', 'pod-template-hash': '747877d66d'}     | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--nginx-proxy-75457c946b     | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--nginx-proxy', 'pod-template-hash': '75457c946b'}     | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--nginx-proxy-76c5f6469b     | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--nginx-proxy', 'pod-template-hash': '76c5f6469b'}     | mapfre-dig-esp--dat--event-sourcing |
| mapfre-dig-esp--dat--pro--nginx-proxy-79ff49d4dc     | europe-west1 | {'app': 'mapfre-dig-esp--dat--pro--nginx-proxy', 'pod-template-hash': '79ff49d4dc'}     | mapfre-dig-esp--dat--event-sourcing |