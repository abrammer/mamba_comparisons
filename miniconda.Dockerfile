FROM condaforge/miniforge3:23.1.0-1
ADD environments ./environments
ARG ENV_FILE

RUN conda env create -f ${ENV_FILE}
