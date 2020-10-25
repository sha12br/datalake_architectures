# Realtime Streaming and Processing of MySQL to Snowflake via Confluent Platform
### MYSQL-->CONFLUENT-->S3 -->AWS LAMBDA-->SNOWFLAKE

### View the Architecture Flow here --> https://github.com/sha12br/datalake_architectures/blob/master/confluent_kafka/mysql-confluent-lambda-snowflake/mysql_ck_lambda_snowflake.JPG

#### Prerequisites

#### ---------------------------------MySQL----------------------------------------------------------------------
##### [mysqld] server-id = 1 
##### log_bin = /var/log/mysql/mysql-bin.log 
##### expire_logs_days = 10 
##### max_binlog_size = 100M 
##### binlog-format = row

##### If it's a RDS --> change the 'BINLOG_FORMAT' from the RDS parameters group to 'ROW'

#### ---------------------------------AWS S3----------------------------------------------------------------------
##### Create a Bucket in S3; Attach policies to this bucket, such that CP can access this from the localhost [Possibly not needed if using AWS access and secret keys]


#### ---------------------------------AWS Lambda----------------------------------------------------------------------
##### Create a Lambda function with proper IAM role to have full access on S3  --> name : "lambda_snowflake_connect"
##### upload the snow_lambda.zip from the repo to the bucket
##### Install awscli in your local host -- > sudo apt-get install awscli [for Ubuntu Machines]
##### Configure the aws environment --> $ aws configure   ==> give away your ACCESS and SECRET Keys; also the region
##### type --> $ aws lambda update-function-code --function-name lambda_snowflake_connect --region us-east-1 --s3-bucket bucket_name --s3-key snow_lambda.zip
##### For more details on how to connect to snowflake from AWS Lambda view this --> https://community.snowflake.com/s/article/How-to-Use-Snowflake-with-AWS-Lambda
##### Create a S3 trigger from lambda --> Add triggers --> choose s3 --> choose the Bucket --> choose "All objects create event" option; add some prefix[from the path for the lambda to trigger ] ex: kafka_topics/
##### lambda function is ready to get triggered!!!!


#### ---------------------------------Confluent Platform----------------------------------------------------------------------
##### Should have > JAVA 1.8 ; conifgure the JAVA_HOME
##### Download the latest version of CP from https://www.confluent.io/download
##### Extract the TAR file 
##### Install the latest CP CLI -- > curl -sL https://cnfl.io/cli | sh -s -- -l
##### Configure CONFLUENT_HOME = 'path to extracted confluent'   ex: '~/confluent-5.5.1/confluent/'
##### Configure the PATH=$CONFLUENT_HOME/bin:$PATH
##### Type 'confluent' in the terminal to view options
##### Type --> $ confluent local services start     ==> to spin up all the services under CP
##### To view more CLI commands --> https://docs.confluent.io/current/confluent-cli/command-reference/index.html
##### Install the debezium mysql connector from confluent-hu -- > $ confluent-hub install debezium/debezium-connector-mysql:latest
##### download the config's json from the repo
##### Type --> $ confluent local services connect connector load mysql_deb.json -c mysql_deb.json
##### check the connector status --> $ confluent local services connect connector status mysql_deb      
##### | NOTE: Should be in a running status; if not troubleshoot from logs --> probably from /tmp/confluent.<some_temp_id>/connect/logs/
##### Tables now would be created as a separate topics in CP check the kafka-topics --> kafka-topics --zookeeper localhost:2181 --list

##### For S3 connect Type --> $ confluent local services connect connector load mysql_s3.json -c mysql_s3.json
##### check the connector status --> $ confluent local services connect connector status mysql_s3    
##### | NOTE: Should be in a running status; if not troubleshoot from logs --> probably from /tmp/confluent.<some_temp_id>/connect/logs/
##### There would be a new folder created "kafka_topics" under which you will your topics i.e. tables and files would be streaming in JSON format.
##### The above streaming JSON files are taken as events into lambda function and processed there and would execute into Snowflake; where you could verify the tables you subscribed to

##### Please review the config JSONS's settings as they may change for users respectively.


