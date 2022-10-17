FROM python:latest
ADD . ./home/helpet/
ENV LD_LIBRARY_PATH=/home/helpet/oracle/:/home/helpet/oracle/instantclient_21_7/
ENV TNS_ADMIN=/home/helpet/oracle/
ENV PORT=9090
EXPOSE 9090
RUN unzip ./home/helpet/oracle/instantclient-basic-linux.x64-21.7.0.0.0dbru.zip -d ./home/helpet/oracle
RUN apt-get update && apt-get install libaio1
RUN pip install django && pip install cx_Oracle && pip install gunicorn && pip install whitenoise
CMD cd ./home/helpet/ && gunicorn --bind 0.0.0.0:$PORT helpet.wsgi
