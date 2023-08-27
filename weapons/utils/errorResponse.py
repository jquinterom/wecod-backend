from rest_framework.response import Response
from rest_framework import status


def errorNotFound(message):
    return Response({"error": True, "message": message}, status=status.HTTP_404_NOT_FOUND)


def errorServer():
    return Response(
        {"error": True, "message": "Error on server, please retry later", },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
