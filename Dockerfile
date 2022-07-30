FROM python:3.7.6
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
COPY .streamlit ./.streamlit
CMD streamlit run app.py --server.port 8501 --server.baseUrlPath /streamlit/