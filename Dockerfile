FROM python:3
RUN git clone https://github.com/Lucasgarciamdz/palindromos-Lucasgarciamdz.git
WORKDIR palindromos-Lucasgarciamdz
RUN pip install -r requirements.txt
CMD ["python3", "test_palindromos.py"]