from django.conf.urls import url
from issue_list.views import GitIssueList

urlpatterns = [
    url(r'^$', GitIssueList.as_view()),
    url(r'^issues', GitIssueList.as_view()),
]
