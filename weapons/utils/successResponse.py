from rest_framework.response import Response
from rest_framework import status


def successResponse(message, data):
    return Response({"error": False, "message": message, "data": data}, status=status.HTTP_200_OK)
