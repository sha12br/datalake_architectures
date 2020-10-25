# Realtime Streaming and Processing of MySQL to Snowflake via Confluent Platform
### MYSQL-->CONFLUENT-->AWS LAMBDA-->SNOWFLAKE

### View the Architecture Flow here --> https://github.com/sha12br/datalake_architectures/blob/master/confluent_kafka/mysql-confluent-lambda-snowflake/mysql_ck_lambda_snowflake.JPG

#### Prerequisites

#### MySQL
##### [mysqld] server-id = 1 
##### log_bin = /var/log/mysql/mysql-bin.log 
##### expire_logs_days = 10 
##### max_binlog_size = 100M 
##### binlog-format = row

##### If it's a RDS --> change the 'BINLOG_FORMAT' from the RDS parameters group to 'ROW'


