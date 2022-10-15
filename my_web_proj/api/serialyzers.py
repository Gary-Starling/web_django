
from rest_framework import serializers  # json
from database.models import UsersInTeam # для модели представленияы


class UserSerialyzer(serializers.ModelSerializer):

    # Модель представления данных будет нашего типа из datbase.models.py

    class Meta:
        model = UsersInTeam  
        fields = ['id', 'name', 'age', 'date_reg']
    '''
    def create(self, validated_data):
        return UsersInTeam.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.age = validated_data.get("age", instance.age)
        instance.date_reg = validated_data.get("date_reg", instance.date_reg)
        instance.save()
        return instance

    def delete(self, instannce, validated_data):
        instannce.id = validated_data.get("id", instannce.id)
        instannce.delete()
        return instannce
    '''