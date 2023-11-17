from todo.models import Task,TaskList
from django.shortcuts import redirect,render,HttpResponse
from django.contrib import messages
from todo.utils import  staff_check
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# @user_passes_test(staff_check)
@login_required

def create_default_tasks(instance, list_id: int):
    task_list = get_object_or_404(TaskList, id=list_id)
    
    # Get the superuser
    superuser = User.objects.filter(is_superuser=True).first()
    
    # Define the default tasks
    default_tasks_data = [
        {"title": "Complete the onboarding process", "description": "Follow the steps provided to get acquainted with our system."},
        {"title": "Meet with your team leader", "description": "Schedule a meeting with your team leader to understand your role."},
        {"title": "Upload Cv/Resume", "description": "Upload your CV for profile verification"},
        # Add more default tasks here
    ]

    # Create task objects and save them to the database for each user
    for task_data in default_tasks_data:

        task = Task(
            title=task_data["title"],
            note=task_data["description"],
            created_by=superuser,
            assigned_to=instance,
            task_list=task_list,
            priority=999,  # Default priority
        )
        task.save()
        print()
            


# @receiver(user_logged_in)
# def user_logged_in_handler(sender, request, user, **kwargs):
#     # Check if the user is part of the specific group
#     specific_group, created = Group.objects.get_or_create(name='Onboarding1')
#     user.groups.add(specific_group)
#     if user.groups.filter(name='Onboarding1').exists():
#         # Get or create the "Onboarding" task list
        
#         task_list, created = TaskList.objects.get_or_create(name="Tasklist", group=specific_group)

#         # Call the function to create default tasks
#         create_default_tasks(request, task_list.id)
#     redirect('todo:lists')
 # Redirect to a relevant page
    