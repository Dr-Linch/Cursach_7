from django.urls import path
from habitsapp.views import (HabitCreateAPIView, PublicHabitListAPIView, SelfHabitListAPIView, HabitRetrieveAPIView,
                              HabitUpdateAPIView, HabitDestroyAPIView)
from habitsapp.apps import HabitsappConfig

app_name = HabitsappConfig.name

urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='create_habit'),
    path('public/habits/list/', PublicHabitListAPIView.as_view(), name='public_habits'),
    path('self/habits/list/', SelfHabitListAPIView.as_view(), name='self_habits'),
    path('habit/<int:pk>/retrieve/', HabitRetrieveAPIView.as_view(), name='retrieve_habit'),
    path('habit/<int:pk>/update/', HabitUpdateAPIView.as_view(), name='update_habit'),
    path('habit/<int:pk>/destroy/', HabitDestroyAPIView.as_view(), name='destroy_habit'),
]