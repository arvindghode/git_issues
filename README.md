#### Finding number of open issues.

This script mainly solves following tasks.

  - Total number of open issues
  - Number of open issues that were opened in the last 24 hours
  - Number of open issues that were opened more than 24 hours ago but less than 7 days ago
  -  Number of open issues that were opened more than 7 days ago

This application is implemented in python and django and hosted on heroku.
To solve this used python libraries.

- django(framework), urllib2, json and datetime.
- also used bootstrap for css.

Using github api we can get issue list, using the list we can get the number of open issues. Passing parameter `since` with the api we can get the issues which are opened in given time span.

Below is the link for live application:
https://protected-river-5492.herokuapp.com/

##### improvement for the current solution
currently im getting the issues individually for each condition which will take much time since its making 3 requests to github. Improvement for this I found is we can get all the issues in one request which will give us a JSON response by parsing the JSON we can easily saperate the open issues since it will make only one API request will be time consuming. 
