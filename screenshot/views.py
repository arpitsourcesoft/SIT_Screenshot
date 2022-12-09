from django.shortcuts import render

#   Importing Liberaries
import time
import pyscreenshot as ImageGrab
import schedule
from datetime import datetime

# Create your views here.
import requests
import time
from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from screenshot.serializers import ScreenShotSerializer

# source_soft_api = 'https://sitemployee.sourcesoftsolutions.com/services/saveAttendanceStatus'
# source_soft_api = 'https://us2.sourcesoftsolutions.com/sit_employee_dev/services/saveAttendanceStatus'

source_soft_api= 'https://us2.sourcesoftsolutions.com/sit_employee_dev/services/saveScreenshotStatus'

get_headers = {'Api-Access-Key': '4AB8N3RS4JSD64FF7A030CO65H23LNAS13JD5478'}

post_headers = {'Content-type': 'multipart/form-data',
                'Api-Access-Key': '4AB8N3RS4JSD64FF7A030CO65H23LNAS13JD5478'}

class ScreenShotView(APIView):
    
    def post(self, request, emp_id):

        def __init__(self):
            self.known_face_encodings = []
            self.known_face_names = []

            # Resize frame for a faster speed
            self.frame_resizing = 0.25
        
        # def take_screenshot():
            emp_id = emp_id
            employee_id = {'emp_id':emp_id}

            response = requests.get('https://us2.sourcesoftsolutions.com/sit_employee_dev/services/getFaceImages',
                                    headers=get_headers, params=employee_id)
            print('response: ', response)
            emp_data = response.json()
            print('emp_data: ', emp_data)

            emp_id = emp_data['data']['emp_id']
            print('emp_id: ', emp_id)
            employee_name = emp_data['data']['first_name']

            image_name = f"screenshot-{str(datetime.now())}"
            screenshot = ImageGrab.grab()
            print('screenshot: ', screenshot)

            filepath = f"./screenshots/{image_name}.png"

            screenshot.save(filepath)

            print("Screenshot taken...")

            # return filepath

            # take_screenshot()
            
            try:
                requests.post(url=source_soft_api,
                              headers=post_headers)
            except Exception as e:
                msz = e
                # pass

            responsedata = {
                'status': 'True',
                'message': msz,
                'success': True,
                # 'response': {'data': {}}
            }
            return Response(responsedata, status=status.HTTP_200_OK)

        responsedata = {
            'status': 'False',
            'message': 'msz'
        }
        return Response(responsedata, status=status.HTTP_400_BAD_REQUEST)
