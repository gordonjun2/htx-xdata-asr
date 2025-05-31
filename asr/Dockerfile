FROM python:3.13.3-slim

ARG INCLUDE_ZSCALER=false

WORKDIR /app
COPY . .

RUN if [ "$INCLUDE_ZSCALER" = "true" ]; then \
      cp ZscalerRootCertificate-2048-SHA256.crt /usr/local/share/ca-certificates/ZscalerRootCertificate-2048-SHA256.crt && \
      update-ca-certificates; \
    fi

# COPY ZscalerRootCertificate-2048-SHA256.crt /usr/local/share/ca-certificates/ZscalerRootCertificate-2048-SHA256.crt

RUN apt-get update && \
    apt-get install -y --no-install-recommends libgomp1 ca-certificates curl && \
    apt-get clean

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001

CMD ["python", "asr_api.py"]
