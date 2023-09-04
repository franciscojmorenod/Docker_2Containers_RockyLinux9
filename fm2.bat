cls
docker stop fmrocky9-container1
docker container rm fmrocky9-container1

docker stop fmrocky9-container2
docker container rm fmrocky9-container2

docker rmi fmrocky9-image1

docker image build -t fmrocky9-image1 .     
docker run -d --name fmrocky9-container1 --privileged --volume=/sys/fs/cgroup:/sys/fs/cgroup:rw --cgroupns=host -e TIMEZONE=America/New_York -e ROOT_PASSWORD=root -P fmrocky9-image1  
docker run -d --name fmrocky9-container2 --privileged --volume=/sys/fs/cgroup:/sys/fs/cgroup:rw --cgroupns=host -e TIMEZONE=America/New_York -e ROOT_PASSWORD=root -P fmrocky9-image1  

docker exec --workdir /run fmrocky9-container1 rm nologin
docker exec --workdir /run fmrocky9-container2 rm nologin
docker exec --workdir /home fmrocky9-container1 python3 hello.py

docker container logs fmrocky9-container1
docker container logs fmrocky9-container2

docker ps -a
docker port fmrocky9-container1
docker port fmrocky9-container2
