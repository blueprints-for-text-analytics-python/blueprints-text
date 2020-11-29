FROM continuumio/miniconda3

# Add environment.yml to the build context and create the environment
ARG conda_env=blueprints
ADD environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml

# Activating the environment and starting the jupyter notebook
RUN echo "source activate ${conda_env}" > ~/.bashrc
ENV PATH /opt/conda/envs/${conda_env}/bin:$PATH

# Start jupyter server on container
EXPOSE 8888
ENTRYPOINT ["jupyter","notebook","--ip=0.0.0.0","--port=8888","--allow-root","--no-browser"]
