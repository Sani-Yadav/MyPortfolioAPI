from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import About, Skill, Project, Education, Experience, Contact
from myproject.serializers import (
    AboutSerializer,
    SkillSerializer,
    ProjectSerializer,
    EducationSerializer,
    ExperienceSerializer,
    ContactSerializer
)

# ✅ PUBLIC GET + Admin CRUD
class AboutView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        about = About.objects.first()
        if not about:
            return Response({"error": "No about information found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AboutSerializer(about)
        return Response(serializer.data)

    def post(self, request):
        # Check if About record already exists
        existing_about = About.objects.first()
        if existing_about:
            return Response(
                {"error": "About information already exists. Use PUT/PATCH to update."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = AboutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        about = About.objects.first()
        if not about:
            return Response({"error": "No about information found to update"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AboutSerializer(about, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        about = About.objects.first()
        if not about:
            return Response({"error": "No about information found to update"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AboutSerializer(about, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Reusable ListCreateAPIView style for other models
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class SkillListCreate(ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SkillDetail(RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProjectListCreate(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProjectDetail(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EducationListCreate(ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EducationDetail(RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ExperienceListCreate(ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ExperienceDetail(RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ContactCreate(APIView):  # Only POST
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Message sent successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            token = Token.objects.get(key=response.data['token'])
            return Response({
                'token': token.key,
                'user_id': token.user.id,
                'username': token.user.username,
                'message': 'Login successful'
            })
        except Exception as e:
            return Response({
                'error': 'Invalid credentials',
                'message': 'Please check your username and password'
            }, status=status.HTTP_400_BAD_REQUEST)
