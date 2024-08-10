from django.db import models

from apps.accounts.models import Employee
from apps.core.models import UUIDModel, TimeStampedModel


# Create your models here.
class Department(UUIDModel):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class PerformanceObjective(UUIDModel, TimeStampedModel):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="objectives"
    )
    description = models.TextField()
    deliverables = models.TextField()
    success_criteria = models.TextField()
    kpis = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.description


class PerformanceReview(UUIDModel, TimeStampedModel):
    achieved = models.BooleanField()
    performance_assessment = models.TextField()
    achievements_and_challenges = models.TextField()
    overall_performance_rating = models.CharField(max_length=50)
    objective = models.ForeignKey(
        PerformanceObjective, on_delete=models.CASCADE, related_name="reviews"
    )

    def __str__(self):
        return f"Review for {self.objective.description}"


class DevelopmentPlan(UUIDModel, TimeStampedModel):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="development_plans"
    )
    current_skills_to_enhance = models.TextField()
    new_skills_to_acquire = models.TextField()
    learning_activities = models.TextField()
    resources_required = models.TextField()
    were_skills_enhanced = models.BooleanField(default=False)
    were_skills_acquired = models.BooleanField(default=False)
    were_activities_accomplished = models.BooleanField(default=False)
    were_resources_provided = models.BooleanField(default=False)

    def __str__(self):
        return f"Development Plan for {self.employee.name}"


class BehaviourAndSkills(UUIDModel, TimeStampedModel):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="behaviour_skills"
    )
    behavioural_expectations = models.TextField()
    improvements = models.TextField(blank=True, null=True)
    aspects_that_need_change = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Behaviour and Skills for {self.employee.name}"


class SupervisorFeedback(UUIDModel, TimeStampedModel):
    reviews = models.ForeignKey(
        PerformanceReview, on_delete=models.CASCADE, related_name="feedbacks"
    )
    overall_performance_feedback = models.TextField()
    overall_performance_rating = models.CharField(max_length=50)

    def __str__(self):
        return f"Feedback for {self.employee.name}"
