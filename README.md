# IOT Data Pipeline

**Step 1:** Launch Kafka. IOT devices will push the data that they generate on this endpoint.

```bash
make up c=kafka
```

> You can acess Kowl interface on http://localhost:8080. It is a simple UI to see basic information of your Kafka cluster.

**Step 2:** Create a Kafka topic to store your data. There is a python to help you do it.

```bash
python3.7 -m pip install -r requirements.txt
python3.7 scripts/create_topic.py <TOPIC_NAME> # for the example, we tooke "iot" as the topic name
```

**Step 3:** Launch InfluxDB. InfluxDB is a time series database. It will be used to store all incoming data from our iot devices. Once it is launched, go to the web UI here: http://localhost:8086 to setup the DB.

```bash
make up c=influxdb
```

**Step 4:** Get your INFLUX_TOKEN from the UI of InfluxDB. Go to the **data** tab, and then in the **API Tokens** tab. Get the token and put in a `.env` file with the key name as **INFLUX_TOKEN**.

```bash
INFLUX_TOKEN=<token>
```

**Step 5:** Setup the Telegraf conf (`telegraf/telegraf.conf`). In the outputs section, change the **organization** and **bucket** fields with the value you selected in _Step 3_. In the inputs section, change
change the **topics** field with the value used in _Step 2_. Also make sure to have the correct configuration for the input json data. (`tag_keys`, `json_time_key`, etc.)

**Step 6:** Launch Telegraf. This service will listen to a Kafka topic and populate InfluxDB with any incoming data on that topic.

```bash
make up c=telegraf
```

**Step 7:** Launch the python script simulating a device that generates data. You can now go explore the generated data in InfluxDB.

```bash
python3.7 scripts/producer.py <TOPIC_NAME>
```

To stop a service:

```bash
make down c=<SERVICE_NAME>
```

To see logs of a service:

```bash
make logs c=<SERVICE_NAME>
```
