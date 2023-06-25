from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Product


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    Serializes the User model fields including:
    - _id: The ID of the user.
    - username: The username of the user.
    - email: The email address of the user.
    - name: The name of the user. If the name is empty, the email is used as the name.
    - isAdmin: Indicates whether the user is an admin.

    Methods:
    - get__id(obj): Retrieves the ID of the user object.
    - get_isAdmin(obj): Checks if the user is an admin.
    - get_name(obj): Retrieves the name of the user. If the name is empty, the email is used as the name.
    """

    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['_id', 'username', 'email', 'name', 'isAdmin']

    @staticmethod
    def get__id(obj):
        """
        Retrieves the ID of the user object.

        Parameters:
        - obj: The user object.

        Returns:
        - int: The ID of the user object.
        """
        return obj.id

    @staticmethod
    def get_isAdmin(obj):
        """
        Checks if the user is an admin.

        Parameters:
        - obj: The user object.

        Returns:
        - bool: True if the user is an admin, False otherwise.
        """
        return obj.is_staff

    @staticmethod
    def get_name(obj):
        """
        Retrieves the name of the user. If the name is empty, the email is used as the name.

        Parameters:
        - obj: The user object.

        Returns:
        - str: The name of the user.
        """
        name = obj.first_name

        if name == '':
            name = obj.email

        return name


class UserSerializerWithToken(UserSerializer):
    """
    Serializer for the User model with an additional token field.

    Inherits from UserSerializer and adds a token field to include the user's authentication token.

    Additional Field:
    - token: The authentication token associated with the user.

    Methods:
    - get_token(obj): Retrieves the authentication token for the user.
    """

    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['_id', 'username', 'email', 'name', 'isAdmin', 'token']

    @staticmethod
    def get_token(obj):
        """
        Retrieves the authentication token for the user.

        Parameters:
        - obj: The user object.

        Returns:
        - str: The authentication token.
        """
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.

    Serializes the Product model fields and provides a representation of the product data.

    Meta:
    - model: The Product model class.
    - fields: A special value '__all__' indicating that all fields in the model should be included.

    Note: This serializer assumes that the Product model has been defined.
    """

    class Meta:
        model = Product
        fields = '__all__'
