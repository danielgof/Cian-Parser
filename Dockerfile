FROM python:3
ADD main.py loader.py parse.py parse.py requirements.txt chromedriver_win32/chromedriver.exe /
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "main.py"]