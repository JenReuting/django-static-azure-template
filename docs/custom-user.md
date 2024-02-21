# Overview


This project uses a custom user that inherits from the default Django User model. This allows us to add custom fields to the user model without having to create a new user model from scratch.

We have also changed the user model so that it does not use the username field. Instead, we use the email field as the unique identifier for the user. The logic for this can be found in ~/users/models.py.

Since we have eliminated the username field, we have also needed to update the admin panel logic, including the admin forms and the admin views. This logic can be found in ~/users/admin.py and ~/users/forms.py.