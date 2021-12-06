FROM python:3
ADD main.py /
ADD config.py /
RUN pip install exchangelib
CMD [ "python", "./main.py" ]
