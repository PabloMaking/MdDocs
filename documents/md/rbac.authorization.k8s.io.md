# RbacAuthK8S-GoogleApis

## ClusterRole

| Name                                                                 | Location     | Labels                                                                                                   |
| -------------------------------------------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------- |
| admin                                                                | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| ca-cr-actor                                                          | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| cloud-provider                                                       | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| cluster-admin                                                        | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| cluster-autoscaler                                                   | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| edit                                                                 | europe-west1 | {'rbac.authorization.k8s.io/aggregate-to-admin': 'true', 'kubernetes.io/bootstrapping': 'rbac-defaults'} |
| external-metrics-reader                                              | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| fluentbit-gke-pod-label-reader                                       | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| gce:beta:kubelet-certificate-bootstrap                               | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| gce:beta:kubelet-certificate-rotation                                | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| gce:cloud-provider                                                   | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| gce:gke-metadata-server-reader                                       | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| gke-metrics-agent                                                    | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| kubelet-api-admin                                                    | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| netd                                                                 | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile', 'kubernetes.io/cluster-service': 'true'}                |
| pdcsi-attacher-role                                                  | europe-west1 | {'k8s-app': 'gcp-compute-persistent-disk-csi-driver', 'addonmanager.kubernetes.io/mode': 'Reconcile'}    |
| pdcsi-provisioner-role                                               | europe-west1 | {'k8s-app': 'gcp-compute-persistent-disk-csi-driver', 'addonmanager.kubernetes.io/mode': 'Reconcile'}    |
| pdcsi-resizer-role                                                   | europe-west1 | {'k8s-app': 'gcp-compute-persistent-disk-csi-driver', 'addonmanager.kubernetes.io/mode': 'Reconcile'}    |
| pdcsi-snapshotter-role                                               | europe-west1 | {'k8s-app': 'gcp-compute-persistent-disk-csi-driver', 'addonmanager.kubernetes.io/mode': 'Reconcile'}    |
| read-updateinfo                                                      | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| snapshot-controller-runner                                           | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| system:aggregate-to-admin                                            | europe-west1 | {'rbac.authorization.k8s.io/aggregate-to-admin': 'true', 'kubernetes.io/bootstrapping': 'rbac-defaults'} |
| system:aggregate-to-edit                                             | europe-west1 | {'rbac.authorization.k8s.io/aggregate-to-edit': 'true', 'kubernetes.io/bootstrapping': 'rbac-defaults'}  |
| system:aggregate-to-view                                             | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults', 'rbac.authorization.k8s.io/aggregate-to-view': 'true'}  |
| system:auth-delegator                                                | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:basic-user                                                    | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:certificates.k8s.io:certificatesigningrequests:nodeclient     | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:certificates.k8s.io:certificatesigningrequests:selfnodeclient | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:certificates.k8s.io:kube-apiserver-client-approver            | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:certificates.k8s.io:kube-apiserver-client-kubelet-approver    | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:certificates.k8s.io:kubelet-serving-approver                  | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:certificates.k8s.io:legacy-unknown-approver                   | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:clustermetrics                                                | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| system:controller:attachdetach-controller                            | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:certificate-controller                             | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:clusterrole-aggregation-controller                 | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:cronjob-controller                                 | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:daemon-set-controller                              | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:deployment-controller                              | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:disruption-controller                              | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:endpoint-controller                                | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:endpointslice-controller                           | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:endpointslicemirroring-controller                  | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:ephemeral-volume-controller                        | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:expand-controller                                  | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:generic-garbage-collector                          | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:glbc                                               | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| system:controller:horizontal-pod-autoscaler                          | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:job-controller                                     | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:namespace-controller                               | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:node-controller                                    | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:persistent-volume-binder                           | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:pod-garbage-collector                              | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:pv-protection-controller                           | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:pvc-protection-controller                          | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:replicaset-controller                              | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:replication-controller                             | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:resourcequota-controller                           | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:root-ca-cert-publisher                             | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:route-controller                                   | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:service-account-controller                         | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:service-controller                                 | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:statefulset-controller                             | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:ttl-after-finished-controller                      | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:controller:ttl-controller                                     | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:discovery                                                     | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:gcp-controller-manager                                        | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| system:gke-common-webhooks                                           | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| system:gke-controller                                                | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| system:gke-hpa-actor                                                 | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| system:gke-hpa-service-reader                                        | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| system:gke-master-healthcheck                                        | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| system:gke-master-resourcequota                                      | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| system:gke-uas-collection-reader                                     | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| system:gke-uas-metrics-reader                                        | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| system:glbc-status                                                   | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| system:heapster                                                      | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:kube-aggregator                                               | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:kube-controller-manager                                       | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:kube-dns                                                      | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:kube-dns-autoscaler                                           | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| system:kube-scheduler                                                | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:kubelet-api-admin                                             | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:kubestore-collector                                           | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| system:managed-certificate-controller                                | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| system:master-monitoring-role                                        | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| system:metrics-server                                                | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile', 'kubernetes.io/cluster-service': 'true'}                |
| system:monitoring                                                    | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:node                                                          | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:node-bootstrapper                                             | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:node-problem-detector                                         | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:node-proxier                                                  | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:persistent-volume-provisioner                                 | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:public-info-viewer                                            | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:resource-tracker                                              | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| system:service-account-issuer-discovery                              | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| system:slo-monitor                                                   | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                         |
| system:volume-scheduler                                              | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                         |
| twistlock-view                                                       | europe-west1 | Null                                                                                                     |
| view                                                                 | europe-west1 | {'rbac.authorization.k8s.io/aggregate-to-edit': 'true', 'kubernetes.io/bootstrapping': 'rbac-defaults'}  |

## ClusterRoleBinding

| Name                                                 | Location     | Labels                                                                                                                 |
| ---------------------------------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------- |
| ca-cr                                                | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| cluster-admin                                        | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| cluster-autoscaler                                   | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| cluster-autoscaler-updateinfo                        | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| event-exporter-rb                                    | europe-west1 | {'k8s-app': 'event-exporter', 'addonmanager.kubernetes.io/mode': 'Reconcile', 'kubernetes.io/cluster-service': 'true'} |
| fluentbit-gke-pod-label-reader                       | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| gce:beta:kubelet-certificate-bootstrap               | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| gce:beta:kubelet-certificate-rotation                | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| gce:cloud-provider                                   | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| gce:gke-metadata-server-reader                       | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| gke-metrics-agent                                    | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| kube-apiserver-kubelet-api-admin                     | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| kubelet-bootstrap                                    | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| kubelet-bootstrap-certificate-bootstrap              | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile', 'kubernetes.io/cluster-service': 'true'}                              |
| kubelet-bootstrap-node-bootstrapper                  | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile', 'kubernetes.io/cluster-service': 'true'}                              |
| kubelet-cluster-admin                                | europe-west1 | {'addonmanager.kubernetes.io/mode': 'EnsureExists'}                                                                    |
| kubelet-user-npd-binding                             | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile', 'kubernetes.io/cluster-service': 'true'}                              |
| master-monitoring-role-binding                       | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| metrics-server:system:auth-delegator                 | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile', 'kubernetes.io/cluster-service': 'true'}                              |
| netd                                                 | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile', 'kubernetes.io/cluster-service': 'true'}                              |
| npd-binding                                          | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile', 'kubernetes.io/cluster-service': 'true'}                              |
| pdcsi-controller-attacher-binding                    | europe-west1 | {'k8s-app': 'gcp-compute-persistent-disk-csi-driver', 'addonmanager.kubernetes.io/mode': 'Reconcile'}                  |
| pdcsi-controller-provisioner-binding                 | europe-west1 | {'k8s-app': 'gcp-compute-persistent-disk-csi-driver', 'addonmanager.kubernetes.io/mode': 'Reconcile'}                  |
| pdcsi-controller-resizer-binding                     | europe-west1 | {'k8s-app': 'gcp-compute-persistent-disk-csi-driver', 'addonmanager.kubernetes.io/mode': 'Reconcile'}                  |
| pdcsi-snapshotter-binding                            | europe-west1 | {'k8s-app': 'gcp-compute-persistent-disk-csi-driver', 'addonmanager.kubernetes.io/mode': 'Reconcile'}                  |
| snapshot-controller-role                             | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| system:basic-user                                    | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:clustermetrics                                | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| system:controller:attachdetach-controller            | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:certificate-controller             | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:clusterrole-aggregation-controller | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:cronjob-controller                 | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:daemon-set-controller              | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:deployment-controller              | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:disruption-controller              | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:endpoint-controller                | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:endpointslice-controller           | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:endpointslicemirroring-controller  | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:ephemeral-volume-controller        | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:expand-controller                  | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:generic-garbage-collector          | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:glbc                               | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| system:controller:horizontal-pod-autoscaler          | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:job-controller                     | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:namespace-controller               | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:node-controller                    | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:persistent-volume-binder           | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:pod-garbage-collector              | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:pv-protection-controller           | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:pvc-protection-controller          | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:replicaset-controller              | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:replication-controller             | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:resourcequota-controller           | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:root-ca-cert-publisher             | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:route-controller                   | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:service-account-controller         | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:service-controller                 | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:statefulset-controller             | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:ttl-after-finished-controller      | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:controller:ttl-controller                     | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:discovery                                     | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:gcp-controller-manager                        | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| system:gke-common-webhooks                           | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| system:gke-controller                                | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| system:gke-hpa-actor                                 | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| system:gke-hpa-service-reader                        | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| system:gke-master-healthcheck                        | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| system:gke-master-resourcequota                      | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| system:gke-uas-collection-reader                     | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| system:gke-uas-hpa-controller                        | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| system:gke-uas-metrics-reader                        | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| system:glbc-status                                   | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| system:kube-controller-manager                       | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:kube-dns                                      | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:kube-dns-autoscaler                           | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| system:kube-proxy                                    | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| system:kube-scheduler                                | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:kubestore-collector                           | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| system:managed-certificate-controller                | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| system:metrics-server                                | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile', 'kubernetes.io/cluster-service': 'true'}                              |
| system:monitoring                                    | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:node                                          | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:node-proxier                                  | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:public-info-viewer                            | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:resource-tracker                              | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| system:service-account-issuer-discovery              | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| system:slo-monitor                                   | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |
| system:volume-scheduler                              | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                                       |
| twistlock-view-binding                               | europe-west1 | Null                                                                                                                   |
| uas-hpa-external-metrics-reader                      | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                                       |

## Role

| Name                                           | Location     | Labels                                                                                                |
| ---------------------------------------------- | ------------ | ----------------------------------------------------------------------------------------------------- |
| system:controller:bootstrap-signer             | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                      |
| cloud-provider                                 | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                      |
| extension-apiserver-authentication-reader      | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                      |
| gce:cloud-provider                             | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                      |
| gce:gke-metadata-server-config-reader          | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                      |
| pdcsi-leaderelection                           | europe-west1 | {'k8s-app': 'gcp-compute-persistent-disk-csi-driver', 'addonmanager.kubernetes.io/mode': 'Reconcile'} |
| snapshot-controller-leaderelection             | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                      |
| system::leader-locking-kube-controller-manager | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                      |
| system::leader-locking-kube-scheduler          | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                      |
| system:controller:bootstrap-signer             | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                      |
| system:controller:cloud-provider               | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                      |
| system:controller:glbc                         | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                      |
| system:controller:token-cleaner                | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                      |
| system:gke-kcm-ccm-leader-election             | europe-west1 | Null                                                                                                  |

## RoleBinding

| Name                                              | Location     | Labels                                                                                                |
| ------------------------------------------------- | ------------ | ----------------------------------------------------------------------------------------------------- |
| system:controller:bootstrap-signer                | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                      |
| gce:cloud-provider                                | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                      |
| gce:gke-metadata-server-config-reader             | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                      |
| gce:podsecuritypolicy:gke-metadata-server         | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                      |
| gce:podsecuritypolicy:pdcsi-node-sa               | europe-west1 | {'k8s-app': 'gcp-compute-persistent-disk-csi-driver', 'addonmanager.kubernetes.io/mode': 'Reconcile'} |
| metrics-server-auth-reader                        | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile', 'kubernetes.io/cluster-service': 'true'}             |
| pdcsi-leaderelection-binding                      | europe-west1 | {'k8s-app': 'gcp-compute-persistent-disk-csi-driver', 'addonmanager.kubernetes.io/mode': 'Reconcile'} |
| snapshot-controller-leaderelection                | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                      |
| system::extension-apiserver-authentication-reader | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                      |
| system::leader-locking-kube-controller-manager    | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                      |
| system::leader-locking-kube-scheduler             | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                      |
| system:controller:bootstrap-signer                | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                      |
| system:controller:cloud-provider                  | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                      |
| system:controller:glbc                            | europe-west1 | {'addonmanager.kubernetes.io/mode': 'Reconcile'}                                                      |
| system:controller:token-cleaner                   | europe-west1 | {'kubernetes.io/bootstrapping': 'rbac-defaults'}                                                      |
| system:gke-kcm-ccm-leader-election                | europe-west1 | Null                                                                                                  |