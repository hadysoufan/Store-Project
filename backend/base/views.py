from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializer import ProductSerializer, UserSerializer, UserSerializerWithToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


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


@api_view(['Get'])
def getRoutes(request):
    routes = [
        '/api/products/',
        '/api/products/create/',

        '/api/products/upload',

        '/api/products/<id>/reviews/',

        '/api/products/top/',
        '/api/products/<id>/',

        '/api/products/delete/<id>/',
        '/api/products/<update>/<id>/',
    ]

    return Response(routes)


@api_view(['Get'])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['Get'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['Get'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
