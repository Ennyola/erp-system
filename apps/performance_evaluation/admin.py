from django.contrib import admin

from .models import (
    Department,
    PerformanceObjective,
    PerformanceReview,
    DevelopmentPlan,
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
