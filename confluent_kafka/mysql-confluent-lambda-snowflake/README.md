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

#### Confluent Platform
##### Should have > JAVA 1.8 ; conifgure the JAVA_HOME
##### Download the latest version of CP from https://www.confluent.io/download
##### Extract the TAR file 
##### Install the latest CP CLI -- > curl -sL https://cnfl.io/cli | sh -s -- -l
##### Configure CONFLUENT_HOME = 'path to extracted confluent'   ex: '~/confluent-5.5.1/confluent/'
##### Configure the PATH=$CONFLUENT_HOME/bin:$PATH
##### Type 'confluent' in the terminal to view options
##### Type --> $ confluent local services start     ==> to spin up all the services under CP
##### To view more CLI commands --> https://docs.confluent.io/current/confluent-cli/command-reference/index.html
##### download the config's json from the repo
##### Type --> $ confluent local services connect connector load mysql_deb.json -c mysql_deb.json
##### check the connector status --> $ confluent local services connect connector status mysql_deb      
##### | NOTE: Should be in a running status; if not troubleshoot from logs --> probably from /tmp/confluent.<some_temp_id>/connect/logs/


