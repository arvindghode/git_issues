from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from datetime import datetime, timedelta
import urllib2
import json


class GitIssueList(View):
    """
    This class is used to get the opened issues.
    Renders the home page.
    """

    ## default html template.
    template_name = 'index.html'

    def get(self, request):
        """
        :param request:
        :return: renders page index.html.
        """
        return render(request, self.template_name, {'data': 0})

    def post(self, request):
        """
        :param request:
        :return: data
        """

        ## get the input url.
        input_url = request.POST.get('git_url','').strip()

        ## validate inputs.
        if input_url == '':
            return self.get(request)

        ## split the url by '/' to get the repo.
        url_list = input_url.split('/')

        ## make url to get all the open issues.
        url = "https://api.github.com/repos/"+str(url_list[3])+"/"+str(url_list[4])

        ## request the github to get the response.
        ## Using urllib2 for http request.
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        ## read the response convert it to json.
        response_data = json.loads(response.read())
        total_open_issues = response_data['open_issues_count'] #get the open issue count from json response.

        ## This block of code is used to get the open issues that added 24 hours ago.
        last_24hr = (datetime.now()-timedelta(days=1)).isoformat() # get the iso format of date time.
        ## Make the request url.
        url_24hr = "https://api.github.com/repos/"+str(url_list[3])+"/"+str(url_list[4])+"/issues?since="+last_24hr
        req_24hr = urllib2.Request(url_24hr)
        response_24hr = urllib2.urlopen(req_24hr)
        ## read the response, convert it to json and get the count of issues.
        total_open_issues_24hr = len(json.loads(response_24hr.read()))

        ## This block of code is used to get the open issues that added 7days ago.
        last_7days = (datetime.now()-timedelta(days=7)).isoformat()  # get the iso format of date time.
        ## make request url.
        url_7days = "https://api.github.com/repos/"+str(url_list[3])+"/"+str(url_list[4])+"/issues?since="+last_7days
        req_7days = urllib2.Request(url_7days)
        response_7days = urllib2.urlopen(req_7days)
        ## read the response, convert it to json and get the count of issues.
        total_open_issues_7days = len(json.loads(response_7days.read()))

        ## difference between total_open_issues_7days and total_open_issues_24hr
        ## will get issues opened between 1 day to 7 days.
        issues_24ago_7days = total_open_issues_7days - total_open_issues_24hr

        ## difference between total_open_issues and total_open_issues_7days
        ## will get issues opened more than 7 days.
        issues_open_more_7days = total_open_issues - total_open_issues_7days

        data = {
            'total_open_issues_24hr':total_open_issues_24hr,
            'total_open_issues_7days':total_open_issues_7days,
            'issues_24ago_7days':issues_24ago_7days,
            'issues_open_more_7days':issues_open_more_7days,
            'total_open_issues':total_open_issues,
            'data':1
        }

        return render(request, self.template_name, data)