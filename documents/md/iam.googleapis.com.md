# IAM-GoogleApis

## Role

| Name                                             | Description                                                                  | Permisos                                                                                                                                                  | State |
| ------------------------------------------------ | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| Role custom_role_bq                              | Custom role custom_role_bq created by terraform                              | ['bigquery.tables.create', 'bigquery.tables.get', 'bigquery.tables.update', 'bigquery.tables.updateData']                                                 | GA    |
| Role custom_role_mapfre_data                     | Custom role custom_role_mapfre_data created by terraform                     | ['bigquery.jobs.create', 'bigquery.transfers.update', 'cloudfunctions.functions.call', 'dataflow.jobs.cancel', 'dataflow.jobs.get', 'dataflow.jobs.list'] | GA    |
| Role custom_role_permission_bq_scheduled_queries | Custom role custom_role_permission_bq_scheduled_queries created by terraform | ['bigquery.datasets.get', 'bigquery.jobs.create', 'bigquery.transfers.update']                                                                            | GA    |
| K8s Secrets Updater                              | Role to update the cluster secrets                                           | ['container.clusters.get', 'container.secrets.create', 'container.secrets.list', 'container.secrets.update', 'secretmanager.versions.access']             | GA    |
| K8s Secrets Updater                              | Role to update the cluster secrets                                           | ['container.clusters.get', 'container.secrets.create', 'container.secrets.list', 'container.secrets.update', 'secretmanager.versions.access']             | GA    |

## ServiceAccountKey

| Name                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/sc-dl--dc--from--df-to-bq@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/3b418e595cb53413a3b598305237be14a7517bf7     |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/reprocessing-events@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/293c045b8f88162af2465003d1438442f2957360           |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/autos-price-ranking--sa@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/7ed4702882353dc50622b20db862e19e4d2be218       |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/bq-scheduled-queries@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/d454871e8dc9a53c712c33ccf1513d56d27dbbdf          |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/ps-to-ps-wh-fl-to-bq@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/fd2bba43f8fd413c272917f8aeb1cb8fc2536c14          |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/sops2secretmank8s--091d44@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/7cc4319ca156fa851a20864f0396da6128bfb06d     |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/sc-sftp--dc--from--df-to-bq@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/0d61e479d5b6cdc3f0bf875b94c9f37d7cd66165   |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/wh-bk--dc--from--df-to-bq@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/752cd2f5fa3082a87b5c7eae69876d58008c1261     |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/sc-fa--dc--from--df-to-bq@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/3ec05d4322c9c6f52d33c69e0a5de139113d42cb     |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/business-intelligence@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/377fd001dbf505a59112dc134ddc49251be37ae9         |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/business-intelligence@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/43d3d38e2ffa9d58b2a1e194557c89064d54276d         |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/ps-to-ps-wh-be-to-bq@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/df494dbc94bded0302ca56a8759d20c2d1f03a98          |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/ope-clientes-tc-nba@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/61738cf773e381c5a19e0fceb0bb3c5ac54f8a2d           |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/sops2secretmank8s--9315e5@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/e7e13fa0b7443a1c59f2a0e3943801fe3e4e94ce     |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/scheduled-query-export-csv@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/20431c94a18253cd980aa1ec325365708f27d728    |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/django-consumer--pro@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/e1196bd88168306603e915a44e7f70e3d5604dc7          |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/mapfre-dig-esp--dat--pro--iac@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/8eefdb95a062652c28496d10591a4d39746f3a65 |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/cross-schedulers@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/143e943e5721501536bce5715165beefd18809f2              |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/looker@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/497fef168ed6da4504d4910de919d464a355c62f                        |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/looker@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/680c76c2c57071b48bd294c6b7f8df1a4f7bb685                        |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/looker@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/94551e54ab883bfc7c91afb203973e6a4beac5fc                        |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/ps-to-ps-wh-cb-to-bq@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/54086b95b6e1aec3fbdc8f1da0a9c1d914e95878          |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/mapfre-dig-esp--dat--pro--8620@appspot.gserviceaccount.com/keys/6f00a46f7f9110ca67712dafe37dc8cce62f0527                           |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/batch-raw-st@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/53d1a90998b1cfcc2077f4bd7aa6f58e2a1481e6                  |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/147054572341-compute@developer.gserviceaccount.com/keys/5b7cc123bd1d70ef8f448b48e570950ac87312ff                                   |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/wh-cpd--dc--from--df-to-bq@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/4de0ed1c259b7d936c792ea8dcdf18797398094f    |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/sc-sf--dc--from--df-to-bq@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/d18bcabfce5407c7b5b38c17959f12fdf3f75a4e     |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/django-producer--pro@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/55dd316b4bcb4682ab14bf8b5bfb3a731de9d946          |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/event-sourcing-archive@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/2d02cf8e6c1c4b26211bef0d720dbea86905d220        |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/bq-check-event-tables@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/a7dba96b77bed4560dca9e926a6ce4171c5eab5b         |
| projects/mapfre-dig-esp--dat--pro--8620/serviceAccounts/wh-cb--dc--from--df-to-bq@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com/keys/8c87f65a585ed15df3e90bc8436283d7b4c9a063     |

## ServiceAccount

| Name                                                                                             | Correo                                                                               | State   |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------- |
| Service account to scheduler-delio--djangoconsumer--from--dataflow-to-bigquery                   | sc-dl--dc--from--df-to-bq@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com     | ENABLED |
| Service account to reprocessing-events                                                           | reprocessing-events@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com           | ENABLED |
| Service Account: autos-price-ranking                                                             | autos-price-ranking--sa@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com       | ENABLED |
| Service account to bq-scheduled-queries                                                          | bq-scheduled-queries@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com          | ENABLED |
| Service account to trans--pubsub-to-pubsub--webhook-files-to-bigquery                            | ps-to-ps-wh-fl-to-bq@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com          | ENABLED |
| mapfre-dig-esp--dat--pro--django-consumer - SA for CF that manage Secrets Manager to K8s Secrets | sops2secretmank8s--091d44@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com     | ENABLED |
| Service account to scheduler-sftp--djangoconsumer--from--dataflow-to-bigquery                    | sc-sftp--dc--from--df-to-bq@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com   | ENABLED |
| Service account to webhook-backevents--djangoconsumer--from--dataflow-to-bigquery                | wh-bk--dc--from--df-to-bq@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com     | ENABLED |
| Service account to scheduler-figuresapp--djangoconsumer--from--dataflow-to-bigquery              | sc-fa--dc--from--df-to-bq@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com     | ENABLED |
| Service account to business-intelligence                                                         | business-intelligence@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com         | ENABLED |
| Service account to trans--pubsub-to-pubsub--webhook-backevents-to-bigquery                       | ps-to-ps-wh-be-to-bq@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com          | ENABLED |
| Service account to ope-clientes-tc-nba                                                           | ope-clientes-tc-nba@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com           | ENABLED |
| mapfre-dig-esp--dat--pro--django-producer - SA for CF that manage Secrets Manager to K8s Secrets | sops2secretmank8s--9315e5@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com     | ENABLED |
| Service account to scheduled-query-export-csv                                                    | scheduled-query-export-csv@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com    | ENABLED |
| Service Account for mapfre-dig-esp--dat--pro--django-consumer                                    | django-consumer--pro@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com          | ENABLED |
| Service account for IAC deployments                                                              | mapfre-dig-esp--dat--pro--iac@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com | ENABLED |
| Service account to cross-schedulers mapfre-dig-esp--dat--pro                                     | cross-schedulers@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com              | ENABLED |
| Service account to looker                                                                        | looker@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com                        | ENABLED |
| Service account to trans--pubsub-to-pubsub--webhook-chatbot-to-bigquery                          | ps-to-ps-wh-cb-to-bq@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com          | ENABLED |
| App Engine default service account                                                               | mapfre-dig-esp--dat--pro--8620@appspot.gserviceaccount.com                           | ENABLED |
| Service account to trans--batch-raw-st                                                           | batch-raw-st@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com                  | ENABLED |
| Compute Engine default service account                                                           | 147054572341-compute@developer.gserviceaccount.com                                   | ENABLED |
| Service account to webhook-cpd--djangoconsumer--from--dataflow-to-bigquery                       | wh-cpd--dc--from--df-to-bq@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com    | ENABLED |
| Service account to scheduler-salesforce--djangoconsumer--from--dataflow-to-bigquery              | sc-sf--dc--from--df-to-bq@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com     | ENABLED |
| Service Account for mapfre-dig-esp--dat--pro--django-producer                                    | django-producer--pro@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com          | ENABLED |
| Service account to event-sourcing-archive                                                        | event-sourcing-archive@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com        | ENABLED |
| Service account to bq-check-event-tables                                                         | bq-check-event-tables@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com         | ENABLED |
| Service account to webhook-chatbot--djangoconsumer--from--dataflow-to-bigquery                   | wh-cb--dc--from--df-to-bq@mapfre-dig-esp--dat--pro--8620.iam.gserviceaccount.com     | ENABLED |