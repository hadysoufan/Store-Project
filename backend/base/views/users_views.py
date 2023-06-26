from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from django.contrib.auth.models import User

from base.serializer import UserSerializer, UserSerializerWithToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.hashers import make_password
from rest_framework import status


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom token obtain pair serializer.

    Extends the TokenObtainPairSerializer provided by the rest_framework_simplejwt library.

    validate(attrs):
    - Overrides the validate() method of the base class to include additional data in the token response.
    - Calls the super() method to validate the attributes and obtain the token data.
    - Uses the UserSerializerWithToken to serialize the user data and adds it to the token response.

    Note: This serializer assumes the use of the TokenObtainPairView view class.
    """

    def validate(self, attrs):
        """
        Validate the attributes and include additional data in the token response.

        Args:
        - attrs (dict): The attributes to validate.

        Returns:
        - data (dict): The validated token data, including additional user data.
        """
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    """
    Custom token obtain pair view.

    Extends the TokenObtainPairView provided by the rest_framework_simplejwt library.

    serializer_class:
    - Specifies the serializer class to be used for obtaining the token pair.
    - Uses the custom MyTokenObtainPairSerializer to include additional user data in the token response.

    Note: This view assumes the use of the MyTokenObtainPairSerializer serializer class.
    """
    serializer_class = MyTokenObtainPairSerializer


@api_view(['Post'])
def registerUser(request):
    """
    Register a new user.

    Parameters:
    - request: The HTTP request object containing user registration data in the request data.

    Returns:
    - Response: The HTTP response object with the serialized user data and a success status code if the registration is successful. If a user with the same email already exists, it returns an error message with a status code indicating a bad request.

    """
    data = request.data

    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)

    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    """
    Update the user's profile.

    Parameters:
    - request: The HTTP request object containing the updated user profile data in the request data.

    Returns:
    - Response: The HTTP response object with the serialized user data if the profile update is successful.

    """
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)

    data = request.data 
    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']
    if data['password'] != '':
        user.password = make_password(data['password'])

    user.save()

    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    """
    Retrieve the user's profile.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Response: The HTTP response object with the serialized user data.

    """
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    """
    Retrieve all users.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Response: The HTTP response object with the serialized user data.

    """
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
