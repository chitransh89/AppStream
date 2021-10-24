#AppStream
This app consumes images from Message Brokers like kafka/Google PubSub, run inference and output the results to console. Code has been written in such a way that the model can be easily added in the respective format.

## How to run this app
1. Install docker and docker-compose
2. Clone the repo
3. Create 2 directories named zookeeper_data and kafka_data at any place in your file system
4. Change the directory's ownership to 1001 using `chown 1001 zookkeper_data kafka_data`
5. Go into the cloned repo and build the docker image. If you are running for google pub sub then provide the ENV settings in the Dockerfile Command to build image is  `sudo docker build -t appStream:0.1 .` 
6. Now open docker-compose.yml and edit the volumes in the zookeeper and kafka service. Provide the path as used in Step 3 to the left side of the colon.
7. Ensure nothing is running on the ports 9092 & 29092. Modify the env variables for kafka and model service wherever applicable (name of topic, ports etc.)
8. Now, run the compose file via sudo docker-compose -f dockers/docker-compose-appstreamer.yml up -d
9. For testing, 
   1. Put the test images in a directory
   2. Go to test/producer.py and edit the dir path TEST_IMAGE_DIR where the images have been put
   3. Run python producer.py (assuming that broker is listening on 29092, which is configured in docker-compose-appstreamer)
   4. Output is getting dumped in the console
