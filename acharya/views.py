
from rest_framework import mixins
from rest_framework import generics,status,permissions

from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

import subprocess
import sys
import os
import json

from acharya.serializers import coursesSerializer, subjectSerializer

from acharya.models import Courses, Subjects
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from distutils.ccompiler import new_compiler


class Courses(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Courses.objects.all()
    serializer_class = coursesSerializer

    def get(self, request):
        return self.list(request)

class Subjects(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Subjects.objects.all()
    serializer_class = subjectSerializer

    def get(self, request):
        return self.list(request)


    
    
class Compile(APIView):
    parser_classes = ([JSONParser])



    permission_classes = [AllowAny]

    serializer_class = exerciseSerializer

    def post(self, request, format=None,):

           
        res = request.data
        MAXTIME = 3


        #print(res)

        #print(res["code"])

        x = Exercise.objects.get(id=1)


        #print(x.mode)

        fname = 'program.c'
        file = open('./program.c', 'w')
        file.write(res['code'])
        file.close()

        output = ""
        compiler = ""
        if os.path.isfile('a.out'):
            os.remove('a.out')
        try:
            command = 'gcc %s;exit 0'%(fname)
            #command = "gcc "+fname
            compiler = subprocess.check_output(command, stderr=subprocess.STDOUT,shell=True,universal_newlines=True)
            print("complier output",compiler)
            if os.path.isfile('a.out'):
                command = "./a.out"
                try:
                    output = subprocess.check_output(command,input=x.case1,stderr=subprocess.STDOUT,shell=True,universal_newlines=True,timeout=MAXTIME)
                    print("Run output",output)
                except subprocess.TimeoutExpired:
                    output = "Execution Time out"
                os.remove('a.out')
            
        except:
            output = "Un-expected error"

        resp = [{"compile" : compiler, "output" : output }]

        



        return Response(resp, status=status.HTTP_201_CREATED)

            





            










    

     