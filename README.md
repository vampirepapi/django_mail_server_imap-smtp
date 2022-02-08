# django_mail_server_imap-smtp

***steps:***

 - activate venv 
 - install requirements
 - run `python manage.py migrate django_mailbox` to create
   the required database tables
   
 - run `python manage.py migrate`
 - create super user with valid credentials
 - run server
 - go to admin panel
 - Once you have entered a mailbox to consume, you can easily verify that you have properly configured your mailbox by either:

-   From the Django Admin, using the ‘Get New Mail’ action from the action dropdown on the Mailbox changelist ([http://yourproject.com/admin/django_mailbox/mailbox/](http://yourproject.com/admin/django_mailbox/mailbox/)).
    
-   _Or_  from a shell opened to your project’s directory, using the  `getmail`  management command by running:  `python manage.py getmail`

- to create new emails head to views.py and craft mail
- simply hit homepage to send mail - Status Code - 202 - means emails are send

***

***Note:- still alpha need more improvements, pr are always welcome***

***

 
   
