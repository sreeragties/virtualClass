from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.indexView,name="home"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('login/',views.loginView,name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='home'),name="logout"),
    path('create_class/',views.createClass,name="create_class"),
    path('join_class/',views.joinClass,name="join_class"),
    path('class_page/<str:class_code>/',views.classView,name="class_page"),
    path('join_page/<str:class_code>/',views.joinView,name="join_page"),
    path('upload_notes/<str:class_code>/',views.noteUpload,name="upload_note"),
    path('upload_assignment/<str:class_code>/',views.assignmentUpload,name="upload_assignment"),
    path('delete_notes/<str:class_code>/<int:note_id>/',views.noteDelete,name="delete_note"),
    path('delete_assignment/<str:class_code>/<int:assignment_id>/',views.assignmentDelete,name="delete_assignment"),
    path('submit_assignment/<int:assignment_id>/',views.submitAssignment,name="submit_assignment"),
    path('unsubmit_assignment/<int:assignment_id>/<int:submitted_id>/',views.unsubmitAssignment,name="unsubmit_assignment"),
    path('grade_assignment/<int:assignment_id>/',views.gradeAssignment,name="grade_assignment"),
    path('marks_grade/<int:submit_id>/',views.marksGrade,name="marks_grade"),
    path('delete_class/<str:class_code>/',views.classDelete,name="delete_class"),
    path('unenroll_class/<str:class_code>/',views.classUnenroll,name="unenroll_class")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
