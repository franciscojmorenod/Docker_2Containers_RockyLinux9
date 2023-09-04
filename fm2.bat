cls
rem *******************************************************************
rem **** turn off and reset everything
docker stop fmrocky9-container1
docker container rm fmrocky9-container1

docker stop fmrocky9-container2
docker container rm fmrocky9-container2

docker rmi fmrocky9-image1

rem *******************************************************************
rem **** build the image
docker image build -t fmrocky9-image1 .    

rem *******************************************************************
rem **** create 2 contaners. Each container and the one image we created inside
docker run -d --name fmrocky9-container1 --privileged --volume=/sys/fs/cgroup:/sys/fs/cgroup:rw --cgroupns=host -e TIMEZONE=America/New_York -e ROOT_PASSWORD=root -P fmrocky9-image1  
docker run -d --name fmrocky9-container2 --privileged --volume=/sys/fs/cgroup:/sys/fs/cgroup:rw --cgroupns=host -e TIMEZONE=America/New_York -e ROOT_PASSWORD=root -P fmrocky9-image1  

rem *******************************************************************
rem docker exec --workdir /run fmrocky9-container1 rm nologin
rem docker exec --workdir /run fmrocky9-container2 rm nologin

rem *******************************************************************
rem run a hello python program
rem docker exec --workdir /home fmrocky9-container1 python3 hello.py

rem *******************************************************************
rem display containers logs
docker container logs fmrocky9-container1
docker container logs fmrocky9-container2

rem *******************************************************************
rem **** display all containers
docker ps -a

rem *******************************************************************
rem **** List port mappings or a specific mapping for the container
docker port fmrocky9-container1
docker port fmrocky9-container2
