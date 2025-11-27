from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
    def validate(self, date):
            current_year = date.today().year
            if date > current_year:
                raise serializers.ValidationError("Publication year cannot be in the future")
            return date
    
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = 'name'