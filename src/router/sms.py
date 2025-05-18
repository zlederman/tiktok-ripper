from fastapi import APIRouter, Depends, Form, Response
from twilio.twiml.messaging_response import MessagingResponse

from src.dependencies.settings import AppSettings, get_settings

sms_router = APIRouter(prefix='/sms')

@sms_router.get('/')
def sms_webhook(From: str = Form(...), Body: str = Form(...), settings: AppSettings = Depends(get_settings)):

   response = MessagingResponse() 
   msg = response.message(f"Hi {From}, you said: {Body}")
   return Response(content=str(response), media_type="application/xml")