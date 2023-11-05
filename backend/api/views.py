from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.parsers import FileUploadParser
from .serializers import TransactionSerializer
from .models import Transaction, Student
from utils.handle import read_excel_file

# Create your views here.
def manage_data(json_data, bus_number, year, monthly):
    data = []
    
    for row in json_data:
        each_row = {}
        student = {}
        student["student_id"] = row['student_id']
        student["firstname"] = row['firstname']
        student["lastname"] = row['lastname']
        student["nickname"] = row['nickname']
        student["level"] = row['level']
        student["bus_number"] = bus_number
        
        each_row['student'] = student
        each_row['price'] = int(row['price'])
        each_row['paid_amount'] = int(row['paid_amount'])
        each_row['description'] = row['description']
        each_row['month'] = row['month']
        each_row['year'] = year
        each_row['monthly'] = monthly
        
        data.append(each_row)
    print(data, len(data))
    return data

class create_view(generics.CreateAPIView, generics.GenericAPIView):
    print(' in lcass')
    # parser_classes = [FileUploadParser]
    
    # def post(self, request, *args, **kwargs):
    #     excel_file = request.FILES["excel_file"] 
    #     json_data, bus_number = read_excel_file(excel_file) 
    #     ready_data = manage_data(json_data, bus_number, request.data.get('year'), request.data.get('monthly'))
        
        # serializer = TransactionSerializer(data=sel)
            
        # if TransactionSerializer.is_valid(raise_exception=True):
        #     student_data = serializer.validated_data['student']
        #     student, created = Student.objects.get_or_create(
        #         student_id= student_data.get("student_id"),
        #         defaults= student_data
        #     )
            
        # serializer.save()
        
        # return super().post(request, *args, **kwargs)
        
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    

           
            
