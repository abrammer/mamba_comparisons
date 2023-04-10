FROM condaforge/mambaforge:23.1.0-1

ADD environments ./environments
ARG ENV_FILE

RUN mamba env create -f ${ENV_FILE}
