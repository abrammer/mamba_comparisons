FROM condaforge/miniforge3:23.1.0-1
ADD environments ./environments
ARG ENV_FILE


RUN conda install -n base conda-libmamba-solver && conda config --set solver libmamba
RUN conda env create -f ${ENV_FILE}
