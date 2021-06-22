FROM python:3.6-slim
COPY . /hometask_3/tests
WORKDIR /tests
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "tests/test_page2.py", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null