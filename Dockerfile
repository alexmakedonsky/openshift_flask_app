FROM python:3.8

WORKDIR /app/

# install env
ADD requirements.txt .
RUN pip install -r requirements.txt

# add service files
COPY . /app/

# set up startup options
ENV FLASK_APP "/app/app.py"
RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
