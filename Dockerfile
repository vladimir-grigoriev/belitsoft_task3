FROM python:3.6-slim
COPY . /hometask_3
WORKDIR /hometask
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "tests/", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null