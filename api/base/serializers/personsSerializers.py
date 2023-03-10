from rest_framework import serializers
from django.contrib.auth.models import User
from api.sales.models import Client,Vendor
from api.schoolfees.models import Student
from api.manage.models import UsersDb, Company, User, ConnectDb

###--------------User--------------------------------
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id']

###----------- Sales---------------------------------
class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        exclude = ('status','created','updated')


class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        exclude = ('status','created','updated')

###----------- School Fees---------------------------------
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        #fields = '__all__'
        exclude = ('status','created','updated') 

###----------- Manage ---------------------------------
class UserDbSerializer(serializers.ModelSerializer):
#class UserDbSerializer(serializers.HyperlinkedModelSerializer):
    #user = serializers.SlugRelatedField(slug_field="name", queryset=User.objects.all())
    company_name= serializers.ReadOnlyField()
    user_name= serializers.ReadOnlyField()
    class Meta:
        model = UsersDb
        #fields = '__all__'
        exclude = ('status','created','updated') 

    """ def to_representation(self,instance):
        data = super().to_representation(instance)
        
        return {
                'url' : data['url'],
                'id'     : instance.id,
                'Nombre': instance.name,
                'Base de Datos' : instance.code,
                'Compañia' : instance.company.name,
                'Compañia Url': data['company'],
                'Usuario' : instance.user.name,
                'Usuario Url': data['user'],
                'Conexion' : instance.connect.name,
                'Conexion Url': data['connect']
        } """  