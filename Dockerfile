FROM tensorflow/tensorflow
RUN pip3 install Scipy
RUN pip3 install Pillow
COPY MLCode/  /root/MLCode
WORKDIR /root/MLCode
CMD python3 ImageclassificationCNN.py