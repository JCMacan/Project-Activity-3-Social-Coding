FROM python
RUN pip install flask
COPY  ./static /home/myapp/static/
COPY  ./templates /home/myapp/templates/
COPY  ip.py /home/myapp/
EXPOSE 5000
CMD python3 /home/myapp/ip.py

