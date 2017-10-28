FROM java:8

# Anaconda3 Install
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh

RUN apt-get install -y curl grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

ENV PATH /opt/conda/bin:$PATH

# App Install
ENV APP_HOME /usr/src/app
COPY . $APP_HOME/
COPY jupyter_notebook_config.py $HOME/.jupyter/

WORKDIR $APP_HOME

RUN conda install --yes --file requirements/python35.txt

COPY docker-entrypoint.sh /usr/local/bin/

# For backwards compatibility
RUN ln -s usr/local/bin/docker-entrypoint.sh /

ENTRYPOINT [ "/usr/bin/tini", "--", "/usr/local/bin/docker-entrypoint.sh" ]
CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser"]
