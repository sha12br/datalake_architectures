#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import boto3

from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import DeleteRowsEvent, UpdateRowsEvent, WriteRowsEvent


def main():
    kinesis = boto3.client('kinesis',region_name='ap-south-1')
    print(kinesis.list_streams())
    print("Entered Main")
    stream = BinLogStreamReader(connection_settings={
        'host': 'url_host',
        'port': 3306,
        'user': 'username',
        'passwd': 'password',
        }, server_id=<server_id>, blocking=True, resume_stream=True,only_schemas=['schema_name'],only_tables=['table1','table2'],
            only_events=[DeleteRowsEvent, WriteRowsEvent,
                UpdateRowsEvent])


    for binlogevent in stream:
        for row in binlogevent.rows:
            event = {
                'schema': binlogevent.schema,
                'table': binlogevent.table,
                'type': type(binlogevent).__name__,
                'row': row,
               }
            kinesis.put_record(StreamName='datastream_name',Data=json.dumps(event),PartitionKey='default')
            print(event)


if __name__ == '__main__':
    main()