from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

#Disease Detection API
@api_view(['POST'])
def detect_disease(request):
    return Response({
        "disease": "Leaf Blight",
        "confidence": 0.92,
        "solution": "Use fungicide within 24 hours"
    })

#Chatbot API
@api_view(['POST'])
def chat(request):
    return Response({
        "reply": "Aapki fasal mein fungal infection ho sakta hai"
    })

#Weather Advice API
@api_view(['GET'])
def weather_advice(request):
    return Response({
        "advice": "Aaj spray na karein, baarish hone wali hai"
    })
