FROM continuumio/anaconda3:4.4.0

ENV APP_HOME /usr/src/app
COPY . $APP_HOME/
COPY jupyter_notebook_config.py $HOME/.jupyter/

WORKDIR $APP_HOME

RUN conda install --yes --file requirements/python35.txt

ENV PATH /usr/local/bin/:$PATH

COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh / # backwards compat

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
