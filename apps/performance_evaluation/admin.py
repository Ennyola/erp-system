from django.contrib import admin

from .models import (
    Department,
    PerformanceObjective,
    PerformanceReview,
    DevelopmentPlan,
    BehaviourAndSkills,
    SupervisorFeedback,
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


@admin.register(PerformanceObjective)
class PerformanceObjectiveAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "description",
        "deliverables",
        "success_criteria",
        "kpis",
        "start_date",
        "end_date",
    )


@admin.register(PerformanceReview)
class PerformanceReviewAdmin(admin.ModelAdmin):
    list_display = (
        "achieved",
        "performance_assessment",
        "achievements_and_challenges",
        "overall_performance_rating",
        "objective",
    )


@admin.register(DevelopmentPlan)
class DevelopmentPlanAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "current_skills_to_enhance",
        "new_skills_to_acquire",
        "new_skills_to_acquire",
    )


@admin.register(BehaviourAndSkills)
class BehviourAndSkillsAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "behavioural_expectations",
        "improvements",
        "aspects_that_need_change",
    )


@admin.register(SupervisorFeedback)
class SupervisorFeedbackAdmin(admin.ModelAdmin):
    list_display = (
        "reviews",
        "overall_performance_feedback",
        "overall_performance_feedback",
    )
