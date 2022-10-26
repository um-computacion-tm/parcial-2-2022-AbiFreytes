FROM python:3
RUN git clone https://github.com/AbiFreytes/Parcial2
WORKDIR /Parcial2
RUN pip install -r requirements.txt
CMD ["python3", "-m", "unittest"]

