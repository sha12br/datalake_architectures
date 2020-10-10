# Data Ingestion from MySQL RDS to S3 --> Amazon Redshift using Amazon Kinesis

# Review the architecture diagram provided in the Repo

# Pre-Requisities

Amazon Kinesis:

Creating a Kinesis Data stream and mapping it to a Kinesis Firehouse Delivery Stream (S3)
AWS console --> Kinesis service --> Data Stream (from the left) --> create a datastream --> give a data stream name and enter the number of shards desired as per the application stream needs --> create the stream

Now for Creating a delivery stream,
Kinesis --> Delivery stream from the left pane
Step 1 : --> Give a delivery stream name , select the source "Kinesis Data Stream" and select the newly created Data Stream from the above step
Step 2: --> This step is optional and could be skipped, unless you want to transform records using lambda or defined schema from AWS Glue Data catalog (Note: For this there has to be a defined schema as table in Datacatalog already)
Step 3: --> Choose destination as "S3" in this case and select the S3 bucket ; you can add prefixes to it.
Step 4: --> Configure the s3 compression if you have specified transformations in step 2; Also buffer interval can be added for the files to arrive with a delay timing;
            Finally choose an IAM role that has policies attached to it appropriately with S3 and AWS Glue datacatalog(if Step 2 is involved)
Step 5: --> Review and Finish ; Takes a min or two to create the delivery stream

RDS MySQL:

