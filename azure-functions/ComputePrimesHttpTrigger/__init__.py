import logging
import azure.functions as func

from . import compute_primes


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    m1 = int(req.params.get('m1'))
    m2 = int(req.params.get('m2'))

    if not m1 or not m2 : 
        return func.HttpResponse(
             "Not a well-formed query",
             status_code=400)

    return func.HttpResponse("The number of primes: " + str(compute_primes.how_many_primes_between(m1, m2)) + "\n")
