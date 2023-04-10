FROM mambaorg/micromamba:1.4
ADD environments ./environments
ARG ENV_FILE

RUN micromamba env create -f ${ENV_FILE}
