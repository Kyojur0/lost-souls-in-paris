from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class TokenGenerator(PasswordResetTokenGenerator):
    """
    TokenGenerator is a custom token generator for generating tokens used in
    password reset functionality. It extends the Django built-in
    PasswordResetTokenGenerator.

    Methods:
    - _make_hash_value: Generates a hash value used to create a unique token.

    Attributes:
    - None

    Example Usage:
    ```python
    generate_token = TokenGenerator()
    token = generate_token.make_token(user_instance)
    ```

    Note: This class is intended for use with Django's default User model.

    References:
    - Django PasswordResetTokenGenerator:
      https://docs.djangoproject.com/en/stable/_modules/django/contrib/auth/tokens/
    - Django Password Reset Documentation:
      https://docs.djangoproject.com/en/stable/topics/auth/passwords/#using-the-reset-password-views
    """
    def _make_hash_value(self, user, timestamp):
        """
        Generates a hash value using the user's primary key, timestamp, and
        the user's active status.

        Parameters:
        - user (User): The user for whom the token is being generated.
        - timestamp (int): The timestamp representing the time of token creation.

        Returns:
        - str: A unique hash value for creating the token.
        """
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )

generate_token = TokenGenerator()
