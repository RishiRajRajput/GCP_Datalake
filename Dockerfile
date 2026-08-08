FROM python:3.11-slim

WORKDIR /opt/project

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "scripts/generate_sample_data.py"]
