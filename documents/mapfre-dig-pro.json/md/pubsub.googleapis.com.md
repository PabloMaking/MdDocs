# PubSub-GoogleApis

## Subscription

| Name                                                                                                                                       | Location |
| ------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| gcf-mapfre-dig-esp--dat--pro--django-producer--sops2secretmank8s-europe-west1-mapfre-dig-esp--dat--pro--django-producer--sops2secretmank8s | global   |
| gcf-mapfre-dig-esp--dat--pro--django-consumer--sops2secretmank8s-europe-west1-mapfre-dig-esp--dat--pro--django-consumer--sops2secretmank8s | global   |
| webhook-backevents--djangoproducer--to--dataflow-to-bigquery.subscription-12891918593787514614                                             | global   |
| scheduler-sftp--djangoproducer--to--dataflow-to-bigquery.subscription-3859320688473939236                                                  | global   |
| scheduler-delio--djangoproducer--to--dataflow-to-bigquery.subscription-3859320688473937648                                                 | global   |
| scheduler-figuresapp--djangoproducer--to--dataflow-to-bigquery.subscription-3859320688473937815                                            | global   |
| webhook-cpd--djangoproducer--to--dataflow-to-bigquery.subscription-3859320688473939069                                                     | global   |
| scheduler-salesforce--djangoproducer--to--dataflow-to-bigquery.subscription-3859320688473936394                                            | global   |

## Topic

| Name                                                             | Location |
| ---------------------------------------------------------------- | -------- |
| scheduler-delio--djangoconsumer--from--dataflow-to-bigquery      | global   |
| scheduler-delio--djangoproducer--to--dataflow-to-bigquery        | global   |
| webhook-cpd--djangoproducer--to--dataflow-to-bigquery            | global   |
| webhook-cpd--djangoconsumer--from--dataflow-to-bigquery          | global   |
| mapfre-dig-esp--dat--pro--django-consumer--sops2secretmank8s     | global   |
| mapfre-dig-esp--dat--pro--django-producer--sops2secretmank8s     | global   |
| webhook-backevents--djangoproducer--to--dataflow-to-bigquery     | global   |
| webhook-backevents--djangoconsumer--from--dataflow-to-bigquery   | global   |
| scheduler-salesforce--djangoproducer--to--dataflow-to-bigquery   | global   |
| scheduler-salesforce--djangoconsumer--from--dataflow-to-bigquery | global   |
| webhook-chatbot--djangoproducer--to--dataflow-to-bigquery        | global   |
| webhook-chatbot--djangoconsumer--from--dataflow-to-bigquery      | global   |
| scheduler-sftp--djangoconsumer--from--dataflow-to-bigquery       | global   |
| scheduler-sftp--djangoproducer--to--dataflow-to-bigquery         | global   |
| scheduler-figuresapp--djangoproducer--to--dataflow-to-bigquery   | global   |
| scheduler-figuresapp--djangoconsumer--from--dataflow-to-bigquery | global   |