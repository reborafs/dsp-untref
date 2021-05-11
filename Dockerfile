# Start from a core stack version
FROM jupyter/base-notebook:latest
# Install in the default python3 environment
RUN pip install --upgrade pip \
pip install numpy \
pip install scipy \
pip install matplotlib 
RUN conda install -c conda-forge pysoundfile
RUN conda install -c conda-forge librosa

COPY TPs dsp/TPs

<<<<<<< HEAD
# Add Tini. Tini operates as a process subreaper for jupyter. This prevents
# kernel crashes.
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

EXPOSE 8888
=======
WORKDIR dsp
>>>>>>> 45302998a59caeeae8e15dbb5b411af084c52c86

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
