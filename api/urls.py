from django.contrib import admin
from django.urls import path
from api.views import ProductViewSet
#from rest_framework import routers
#from django.urls import path,include
from api.schema import schema
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

#router= routers.DefaultRouter()
#router.register(r'products', ProductViewSet)
#urlpatterns = [
#     path('',include(router.urls))
#]





urlpatterns = [
    path("graphql",
              csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
               ]