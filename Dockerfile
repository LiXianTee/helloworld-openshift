FROM selenium/standalone-chrome-debug:3.141.59-yttrium

RUN sudo mkdir /opt/app

WORKDIR /opt

COPY test_oranghrm.py /opt

RUN sudo apt update 

RUN sudo apt install -y software-properties-common

RUN sudo add-apt-repository ppa:deadsnakes/ppa 

RUN sudo apt install -y python3.9 

RUN sudo apt install -y python3-pip

RUN sudo pip3 install --target=/opt/app --system selenium

RUN sudo pip3 install --target=/opt/app --system pytest

RUN sudo pip3 install --target=/opt/app --system allure-pytest

RUN sudo wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.16.1/allure-commandline-2.16.1.tgz

RUN sudo tar -zxvf allure-commandline-2.16.1.tgz -C /opt/

RUN sudo ln -s /opt/allure-2.16.1/bin/allure /usr/bin/allure

RUN sudo chgrp -R 0 /opt && sudo chmod -R g=u /opt

RUN sudo chgrp -R 0 /opt/app && sudo chmod -R g=u /opt/app

RUN sudo chgrp -R 0 /opt/test_oranghrm.py && sudo chmod -R g=u /opt/test_oranghrm.py

RUN sudo chgrp -R 0 /opt/allure-2.16.1 && sudo chmod -R g=u /opt/allure-2.16.1

RUN sudo chgrp -R 0 /usr/bin/allure && sudo chmod -R g=u /usr/bin/allure

#CMD pytest -v -s --alluredir="/opt/app" /opt/test_oranghrm.py

EXPOSE 4444

EXPOSE 5900

ENTRYPOINT ["/opt/bin/entry_point.sh"]








