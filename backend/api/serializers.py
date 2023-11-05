from rest_framework import serializers
from .models import Transaction, Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=False)
    class Meta:
        model = Transaction
        fields = [
            'student',
            'price',
            'paid_amount',
            'description',
            'month',
            'year',
            'monthly',
        ]
        
    def create(self, validated_data):
        print(' in create')
        student_data = validated_data.pop('student')
        student_id = student_data.get('student_id')
        
        student, created = Student.objects.get_or_create(
            student_id=student_id,
            defaults=student_data
        )
        
        if not created:
            student_data.pop('student_id')
            for attr, value in student_data.items():
                if getattr(student, attr) != value :
                    setattr(student, attr, value)
            student.save()
                
        transaction = Transaction.objects.create(student=student,**validated_data)
        
        return transaction
        