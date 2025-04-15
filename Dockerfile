# Based on https://raw.githubusercontent.com/jupyter/docker-stacks/master/scipy-notebook/Dockerfile
ARG BASE_CONTAINER=jupyter/minimal-notebook
FROM $BASE_CONTAINER

USER root

USER $NB_UID

# Install Python 3 packages
RUN conda install \
        bokeh \
        gdal \
        gtsam \
        ipympl \
        jupyterlab \
        nodejs \
        pandas \
        pandas-datareader \
        pip \
        seaborn \
        scikit-learn && \
    conda clean --all -f -y && \
    pip install rosbags geojson && \
    jupyter lab build -y && \
    jupyter lab clean -y && \
    npm cache clean --force && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

USER $NB_UID

WORKDIR $HOME

