FROM python:alpine

COPY script.sh . 
COPY compute_primes.py . 
RUN chmod +x ./script.sh
ENTRYPOINT ["sh", "./script.sh"]
