FROM continuumio/miniconda3

# Add environment.yml to the build context and create the environment
ARG conda_env=sentiment_app
ADD environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml

# Activating the environment and starting the jupyter notebook
RUN echo "source activate ${conda_env}" > ~/.bashrc
ENV PATH /opt/conda/envs/${conda_env}/bin:$PATH

# Copy files required for deploying service to app folder in container
COPY . /app
WORKDIR /app

# Start WSGI server on container
EXPOSE 5000
RUN ["chmod", "+x", "start_script.sh"]
ENTRYPOINT [ "/bin/bash", "-c" ]
CMD ["./start_script.sh"]
