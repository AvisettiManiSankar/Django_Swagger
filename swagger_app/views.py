from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Question
from .serializers import QuestionSerializer

class GetQuestionsView(GenericAPIView):
    serializer_class = QuestionSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of questions.",
        responses={
            200: openapi.Response(
                description="A list of questions",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'status': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Request status'),
                        'msg': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_OBJECT), description='List of questions'),
                        'error': openapi.Schema(type=openapi.TYPE_STRING, description='Error message if any')
                    }
                )
            ),
            400: openapi.Response(
                description="Bad request error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'status': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Request status'),
                        'msg': openapi.Schema(type=openapi.TYPE_STRING, description='Error message'),
                        'error': openapi.Schema(type=openapi.TYPE_STRING, description='Error details')
                    }
                )
            )
        }
    )
    def get(self, request, *args, **kwargs):
        questions = Question.objects.all()
        serializer = self.get_serializer(questions, many=True)
        return Response({
            "status": True,
            "msg": serializer.data,
            "error": ''
        })
