FROM centos

RUN yum update -y
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
RUN yum install deltarpm -y
RUN yum install -y python36u python36u-libs python36u-devel python36u-pip

ADD . /code
WORKDIR . /code

RUN pip3.6 install --upgrade pip
RUN pip3.6 install -r requeriments.txt