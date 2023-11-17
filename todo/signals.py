
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
# from .views import create_default_tasks
from todo.models import Task, TaskList
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# @login_required
# @receiver(user_logged_in)
# def user_logged_in_handler(sender, request, user, **kwargs):
#     print(f"User {user.username} logged in.")
    
    
        
#     if user.groups.filter(name='Onboarding').exists():
#         print("user already exist in Onboarding.")
#     else:
#         specific_group, created = Group.objects.get_or_create(name='Onboarding')
#         user.groups.add(specific_group)
#         task_list, created = TaskList.objects.get_or_create(name="Tasks",group=specific_group,slug='Onboarding')
#         print(f"Task list created: {task_list}")
#         create_default_tasks(request, task_list.id)

@receiver(post_save, sender=User)        
def user_registered_handler(sender, instance, created, **kwargs):
    if created:
        print(f"User {instance.username} registered.")

        if instance.groups.filter(name='Onboarding').exists():
            print("User already exists in Onboarding.")
        else:
            specific_group, group_created = Group.objects.get_or_create(name='Onboarding')
            instance.groups.add(specific_group)
            task_list, task_list_created = TaskList.objects.get_or_create(name="Tasks", group=specific_group, slug='Onboarding')
            print(f"Task list created: {task_list}")
            
            # Assuming create_default_tasks is a function that creates default tasks
            create_default_tasks(instance, task_list.id)

def create_default_tasks(user, list_id: int):
    task_list = get_object_or_404(TaskList, id=list_id)
    superuser = User.objects.filter(is_superuser=True).first()
    if not user.is_superuser or user.is_staff :
    # Define the default tasks
        default_tasks_data = [
            {"title": "Complete the onboarding process", "description": "Follow the steps provided to get acquainted with our system."},
            {"title": "Meet with your team leader", "description": "Schedule a meeting with your team leader to understand your role."},
            {"title": "Upload Cv/Resume", "description": "Upload your CV for profile verification"},
            # Add more default tasks here
        ]
        # Create task objects and save them to the database for the current registered user
        for task_data in default_tasks_data:

            task = Task(
                title=task_data["title"],
                note=task_data["description"],
                created_by=superuser,
                assigned_to=user,  # Assign the task to the registered user
                task_list=task_list,
                priority=999,  # Default priority
            )
            task.save()
            print(f"Task '{task.title}' assigned to {user.username}")
