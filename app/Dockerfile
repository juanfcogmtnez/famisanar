FROM juanfcogmtnez/dominican
RUN rm -r /app
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
RUN pip3 install -r requirements.txt
ADD . /app
EXPOSE 80
ENTRYPOINT ["python", "main.py"]
