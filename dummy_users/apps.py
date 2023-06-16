from django.apps import AppConfig


class DummyUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dummy_users'
    
    def ready(self):
        from dummy_users.models import Profiles

        # Create static data for Student
        student_data = [
            {'name': 'Student 1', 'role': 'S'},
            {'name': 'Student 2', 'role': 'S'},
            # Add more student data here
        ]

        for data in student_data:
            Profiles.objects.get_or_create(**data)

        # Create static data for Teacher
        teacher_data = [
            {'name': 'Teacher 1', 'role': 'T'},
            {'name': 'Teacher 2', 'role': 'T'},
            # Add more teacher data here
        ]

        for data in teacher_data:
            Profiles.objects.get_or_create(**data)
