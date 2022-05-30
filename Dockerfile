FROM tensorflow/tensorflow
RUN pip3 install Scipy
RUN pip3 install Pillow
RUN mkdir /root/ml/
COPY images/*  /root/ml/
WORKDIR /root/ml
CMD python3 ImageclassificationCNN.py
