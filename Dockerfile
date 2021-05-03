# Start from a core stack version
FROM jupyter/base-notebook:latest
# Install in the default python3 environment
RUN pip install --upgrade pip \
pip install numpy \
pip install scipy \
pip install matplotlib 
RUN conda install -c conda-forge pysoundfile
RUN conda install -c conda-forge librosa

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]