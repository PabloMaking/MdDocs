# Logging-GoogleApis

## LogBucket

| Name      | Description    | Location | State  |
| --------- | -------------- | -------- | ------ |
| _Default  | Default bucket | global   | ACTIVE |
| _Required | Audit bucket   | global   | ACTIVE |

## LogSink

| Name                     | Desciption                                                                                                                                                | Location |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| _Default                 | Null                                                                                                                                                      | global   |
| _Required                | Null                                                                                                                                                      | global   |
| dataflow-logs-sink-Files | Routes in real time some specific logs from Dataflow that report the current state of the data sources being processed on Dataflow with the string [File: | global   |