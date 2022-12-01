FROM ubuntu:22.04
ENV PYENV_SHELL=/bin/bash
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN apt-get update && apt-get -y upgrade \
  && apt-get install -y --no-install-recommends \
    git \
    wget \
    g++ \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh 
RUN conda --version
RUN conda init bash
RUN . /root/.bashrc
RUN conda update conda

RUN conda install cuda -c nvidia/label/cuda-11.3.0 -c nvidia/label/cuda-11.3.1
RUN conda install pytorch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 cudatoolkit=11.3 -c pytorch
RUN mkdir -p /app

WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
RUN apt update
RUN apt install sudo
RUN sudo apt-get install -y zip htop screen libgl1-mesa-glx
RUN sudo apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6
COPY . /app

EXPOSE 9000

CMD ["uvicorn", "subprocess_file:app", "--port", "9000","--host", "0.0.0.0","--reload"]