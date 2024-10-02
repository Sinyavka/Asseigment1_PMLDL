FROM python:3.9-slim

WORKDIR /app

# Copy the api.py file into the container
COPY ./api.py /app/api.py

# Install compatible versions of scikit-learn and numpy
RUN pip install fastapi uvicorn joblib scikit-learn==1.2.2 numpy==1.21.6 pydantic

# Start the FastAPI server
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
