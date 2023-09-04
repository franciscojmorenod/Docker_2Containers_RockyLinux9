FROM rockylinux:9
ENV container docker
# see https://hub.docker.com/_/rockylinux 
# RockyLinux:9 missing /usr/sbin/init -> ../lib/systemd/systemd
#  see https://github.com/rocky-linux/sig-cloud-instance-images/issues/39
RUN [ ! -f /usr/sbin/init ] && dnf -y install systemd;
RUN ([ -d /lib/systemd/system/sysinit.target.wants ] && cd /lib/systemd/system/sysinit.target.wants/ && for i in *; do [ $i == \
systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;


RUN dnf -y install net-tools
RUN dnf -y install openssh-server
RUN dnf -y install pip
RUN dnf -y install iputils
RUN dnf -y install nano
RUN pip3 install requests
RUN pip3 install netifaces


RUN useradd --create-home --base-dir /home fjmoreno && echo "fjmoreno:sicurumero" | chpasswd

ENV TIMEZONE America/New_York

ENV ROOT_PASSWORD root

EXPOSE 22

VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/init"]

COPY hello.py /home/.
COPY 123.txt /home/.
COPY TCPserver.py /home/fjmoreno/.
COPY TCPclient.py /home/fjmoreno/.
WORKDIR /home/
RUN python3 hello.py
